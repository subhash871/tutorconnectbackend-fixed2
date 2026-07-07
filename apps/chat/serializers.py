from rest_framework import serializers
from apps.chat.models import Conversation, Message, TypingIndicator
from apps.users.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id', 'conversation', 'sender', 'sender_name', 'content', 
                 'is_read', 'read_at', 'image', 'file', 'created_at']
        read_only_fields = ['id', 'sender', 'is_read', 'read_at', 'created_at']

    def get_sender_name(self, obj):
        return obj.sender.get_full_name()


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['conversation', 'content', 'image', 'file']


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()
    unread_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'booking', 'is_active', 
                 'last_message', 'unread_count', 'created_at', 'updated_at']

    def get_last_message(self, obj):
        message = obj.messages.last()
        if message:
            return MessageSerializer(message).data
        return None

    def get_unread_count(self, obj):
        return obj.messages.filter(is_read=False).exclude(
            sender=self.context['request'].user
        ).count()


class TypingIndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypingIndicator
        fields = ['conversation', 'user', 'is_typing']