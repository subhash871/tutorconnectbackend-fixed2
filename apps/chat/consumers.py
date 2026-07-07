import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    """
    One group per conversation: `chat_<conversation_id>`.

    Client -> server events:
      {"type": "message", "content": "..."}
      {"type": "typing", "is_typing": true}
      {"type": "read"}

    Server -> client events:
      {"type": "message", "message": {...}}
      {"type": "typing", "user_id": N, "is_typing": true}
      {"type": "read", "user_id": N}
      {"type": "error", "detail": "..."}
    """

    async def connect(self):
        self.user = self.scope.get('user')
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.group_name = f'chat_{self.conversation_id}'

        if self.user is None or not self.user.is_authenticated:
            await self.close(code=4001)
            return

        allowed = await self._user_in_conversation()
        if not allowed:
            await self.close(code=4003)
            return

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        event_type = content.get('type')

        if event_type == 'message':
            text = (content.get('content') or '').strip()
            if not text:
                return
            message = await self._create_message(text)
            await self.channel_layer.group_send(self.group_name, {
                'type': 'chat.message',
                'message': message,
            })

        elif event_type == 'typing':
            await self.channel_layer.group_send(self.group_name, {
                'type': 'chat.typing',
                'user_id': self.user.id,
                'is_typing': bool(content.get('is_typing')),
            })

        elif event_type == 'read':
            await self._mark_read()
            await self.channel_layer.group_send(self.group_name, {
                'type': 'chat.read',
                'user_id': self.user.id,
            })

    # --- group event handlers (renamed per Channels' dot-to-underscore rule) ---

    async def chat_message(self, event):
        await self.send_json({'type': 'message', 'message': event['message']})

    async def chat_typing(self, event):
        if event['user_id'] == self.user.id:
            return
        await self.send_json({'type': 'typing', 'user_id': event['user_id'], 'is_typing': event['is_typing']})

    async def chat_read(self, event):
        await self.send_json({'type': 'read', 'user_id': event['user_id']})

    # --- DB helpers ---

    @database_sync_to_async
    def _user_in_conversation(self):
        from apps.chat.models import Conversation
        return Conversation.objects.filter(id=self.conversation_id, participants=self.user).exists()

    @database_sync_to_async
    def _create_message(self, text):
        from apps.chat.models import Conversation, Message
        from apps.chat.serializers import MessageSerializer

        conversation = Conversation.objects.get(id=self.conversation_id)
        message = Message.objects.create(conversation=conversation, sender=self.user, content=text)
        conversation.save(update_fields=['updated_at'])
        return MessageSerializer(message).data

    @database_sync_to_async
    def _mark_read(self):
        from apps.chat.models import Message
        Message.objects.filter(conversation_id=self.conversation_id, is_read=False) \
            .exclude(sender=self.user).update(is_read=True)
