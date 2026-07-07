from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class Conversation(TimeStampedModel):
    """
    Chat conversation between two users.
    """
    participants = models.ManyToManyField(
        'users.User',
        related_name='conversations',
    )
    booking = models.ForeignKey(
        'bookings.Booking',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='conversations',
    )
    is_active = models.BooleanField(_('active'), default=True)
    
    class Meta:
        verbose_name = _('conversation')
        verbose_name_plural = _('conversations')
        ordering = ['-updated_at']

    def __str__(self):
        return f'Conversation {self.id}'


class Message(TimeStampedModel):
    """
    Individual message within a conversation.
    """
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages',
    )
    sender = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='sent_messages',
    )
    content = models.TextField(_('content'), max_length=5000, blank=True)
    is_read = models.BooleanField(_('read'), default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    
    # File attachments
    image = models.FileField(
        upload_to='chat/images/',
        null=True,
        blank=True,
    )
    file = models.FileField(
        upload_to='chat/files/',
        null=True,
        blank=True,
    )
    
    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sender.get_short_name()}: {self.content[:50]}'


class TypingIndicator(models.Model):
    """
    Tracks when a user is typing in a conversation.
    """
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='typing_indicators',
    )
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    is_typing = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['conversation', 'user']