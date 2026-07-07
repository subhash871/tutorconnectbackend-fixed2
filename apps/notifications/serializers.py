from rest_framework import serializers
from apps.notifications.models import Notification, EmailLog, PushDevice


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'notification_type', 'title', 'message', 'data', 
                 'is_read', 'read_at', 'created_at']
        read_only_fields = ['id', 'created_at']


class PushDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushDevice
        fields = ['id', 'device_token', 'device_type', 'is_active']