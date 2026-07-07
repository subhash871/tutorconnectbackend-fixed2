from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.notifications.views import NotificationViewSet, PushDeviceViewSet

app_name = 'notifications'

router = DefaultRouter()
router.register(r'', NotificationViewSet, basename='notification')
router.register(r'devices', PushDeviceViewSet, basename='push-device')

urlpatterns = [
    path('', include(router.urls)),
]