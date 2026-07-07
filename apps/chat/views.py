from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone
from apps.chat.models import Conversation, Message, TypingIndicator
from apps.chat.serializers import (
    ConversationSerializer, MessageSerializer, MessageCreateSerializer,
    TypingIndicatorSerializer
)
from apps.notifications.tasks import create_notification


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Conversation.objects.filter(
            participants=self.request.user
        ).prefetch_related('participants', 'messages')

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)
        other_user_id = self.request.data.get('participant_id')
        if other_user_id:
            conversation.participants.add(other_user_id)

    @action(detail=True, methods=['post'])
    def mark_read(self, request, pk=None):
        conversation = self.get_object()
        conversation.messages.filter(~Q(sender=request.user), is_read=False).update(
            is_read=True, read_at=timezone.now()
        )
        return Response({'message': 'Messages marked as read.'})


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return MessageCreateSerializer
        return MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(
            conversation__participants=self.request.user
        ).select_related('sender')

    def perform_create(self, serializer):
        conversation_id = serializer.validated_data['conversation'].id
        conversation = Conversation.objects.get(id=conversation_id)
        if self.request.user not in conversation.participants.all():
            raise permissions.PermissionDenied('You are not a participant in this conversation.')
        message = serializer.save(sender=self.request.user)
        conversation.save()  # Update updated_at timestamp

        for recipient in conversation.participants.exclude(id=self.request.user.id):
            create_notification.delay(
                recipient.id, 'new_message', f'New message from {self.request.user.get_full_name()}',
                message.content[:200],
                {'conversation_id': conversation.id, 'message_id': message.id},
            )


class TypingIndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = TypingIndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TypingIndicator.objects.filter(
            conversation__participants=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)