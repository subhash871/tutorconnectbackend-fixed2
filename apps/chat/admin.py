from django.contrib import admin
from .models import Conversation, Message, TypingIndicator


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_active', 'booking', 'updated_at', 'created_at']
    list_filter = ['is_active']
    search_fields = ['participants__email', 'booking__booking_id']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'sender', 'content', 'is_read', 'created_at']
    list_filter = ['is_read']
    search_fields = ['sender__email', 'content']


@admin.register(TypingIndicator)
class TypingIndicatorAdmin(admin.ModelAdmin):
    list_display = ['conversation', 'user', 'is_typing', 'updated_at']
    search_fields = ['user__email']
