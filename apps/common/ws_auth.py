"""
JWT authentication middleware for Django Channels.

The REST API uses JWT (SimpleJWT) exclusively — there are no session
cookies. Channels' built-in AuthMiddlewareStack only understands
session-based auth, so without this, every WebSocket connection's
`scope['user']` is AnonymousUser regardless of any token the client
sends, and every consumer that checks `is_authenticated` rejects the
connection immediately.

This middleware reads `?token=<access_token>` from the WebSocket
connection's query string, validates it the same way SimpleJWT does,
and sets scope['user'] to the matching Django user.
"""
from urllib.parse import parse_qs

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser


@database_sync_to_async
def get_user_from_token(token):
    from rest_framework_simplejwt.tokens import AccessToken
    from rest_framework_simplejwt.exceptions import TokenError
    from django.contrib.auth import get_user_model

    User = get_user_model()
    try:
        validated_token = AccessToken(token)
        user_id = validated_token.get('user_id')
        return User.objects.get(id=user_id)
    except (TokenError, User.DoesNotExist, Exception):
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string = scope.get('query_string', b'').decode()
        query_params = parse_qs(query_string)
        token = query_params.get('token', [None])[0]

        if token:
            scope['user'] = await get_user_from_token(token)
        else:
            scope['user'] = AnonymousUser()

        return await super().__call__(scope, receive, send)


def JWTAuthMiddlewareStack(inner):
    return JWTAuthMiddleware(inner)