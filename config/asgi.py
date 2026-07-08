"""
ASGI config for TutorConnect Nepal project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# django_asgi_app must be created before importing anything that touches
# models/apps, so Django's app registry is populated first.
django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter  # noqa: E402
from apps.common.ws_auth import JWTAuthMiddlewareStack  # noqa: E402
import apps.chat.routing  # noqa: E402

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": JWTAuthMiddlewareStack(
        URLRouter(
            apps.chat.routing.websocket_urlpatterns
        )
    ),
})