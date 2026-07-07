from django.contrib import admin
from .models import Notification, EmailLog, PushDevice


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'notification_type', 'title', 'is_read', 'is_email_sent', 'created_at']
    list_filter = ['notification_type', 'is_read', 'is_email_sent']
    search_fields = ['recipient__email', 'title', 'message']


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'subject', 'is_sent', 'sent_at', 'created_at']
    list_filter = ['is_sent']
    search_fields = ['recipient', 'subject']


@admin.register(PushDevice)
class PushDeviceAdmin(admin.ModelAdmin):
    list_display = ['user', 'device_type', 'device_token', 'is_active', 'created_at']
    list_filter = ['device_type', 'is_active']
    search_fields = ['user__email', 'device_token']
