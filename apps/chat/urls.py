from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.chat.views import ConversationViewSet, MessageViewSet, TypingIndicatorViewSet

app_name = 'chat'

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'typing', TypingIndicatorViewSet, basename='typing')

urlpatterns = [
    path('', include(router.urls)),
]