from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class Notification(TimeStampedModel):
    """
    Notification model for in-app notifications.
    """

    class NotificationType(models.TextChoices):
        BOOKING_REQUEST = 'booking_request', _('Booking Request')
        BOOKING_ACCEPTED = 'booking_accepted', _('Booking Accepted')
        BOOKING_REJECTED = 'booking_rejected', _('Booking Rejected')
        BOOKING_CANCELLED = 'booking_cancelled', _('Booking Cancelled')
        BOOKING_COMPLETED = 'booking_completed', _('Booking Completed')
        BOOKING_RESCHEDULED = 'booking_rescheduled', _('Booking Rescheduled')
        PAYMENT_RECEIVED = 'payment_received', _('Payment Received')
        PAYMENT_REFUNDED = 'payment_refunded', _('Payment Refunded')
        NEW_REVIEW = 'new_review', _('New Review')
        NEW_MESSAGE = 'new_message', _('New Message')
        TEACHER_APPROVED = 'teacher_approved', _('Teacher Approved')
        TEACHER_REJECTED = 'teacher_rejected', _('Teacher Rejected')
        WELCOME = 'welcome', _('Welcome')
        REMINDER = 'reminder', _('Reminder')
        SYSTEM = 'system', _('System')

    recipient = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    notification_type = models.CharField(
        _('type'),
        max_length=30,
        choices=NotificationType.choices,
    )
    title = models.CharField(_('title'), max_length=200)
    message = models.TextField(_('message'), max_length=2000)
    data = models.JSONField(_('data'), null=True, blank=True)
    is_read = models.BooleanField(_('read'), default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    is_email_sent = models.BooleanField(_('email sent'), default=False)
    is_push_sent = models.BooleanField(_('push sent'), default=False)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', '-created_at']),
            models.Index(fields=['recipient', 'is_read']),
        ]

    def __str__(self):
        return f'{self.recipient.email} - {self.title}'


class EmailLog(models.Model):
    """
    Log of sent emails.
    """
    recipient = models.EmailField()
    subject = models.CharField(max_length=500)
    body = models.TextField()
    is_sent = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Email to {self.recipient}: {self.subject}'


class PushDevice(models.Model):
    """
    Device token for push notifications.
    """
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='push_devices',
    )
    device_token = models.CharField(max_length=500)
    device_type = models.CharField(
        max_length=10,
        choices=[('ios', 'iOS'), ('android', 'Android'), ('web', 'Web')],
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'device_token']

    def __str__(self):
        return f'{self.user.email} - {self.device_type}'