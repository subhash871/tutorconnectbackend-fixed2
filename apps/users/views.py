from rest_framework import viewsets, status, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.users.models import User, LoginHistory
from apps.users.serializers import (
    UserSerializer, UserProfileSerializer, UserListSerializer, LoginHistorySerializer
)
from apps.common.permissions import IsOwnerOrAdmin, IsAdmin
from apps.notifications.tasks import create_notification


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        if self.action == 'update_profile':
            return UserProfileSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        elif self.action in ['update_profile', 'me', 'login_history', 'deactivate']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [p() for p in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin' or user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)
    
    @action(detail=False, methods=['get', 'put', 'patch'])
    def me(self, request):
        """
        Get or update the current user's profile.
        """
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)
    
    @action(detail=False, methods=['get'])
    def login_history(self, request):
        """
        Get the current user's login history.
        """
        history = LoginHistory.objects.filter(user=request.user)
        serializer = LoginHistorySerializer(history, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def deactivate(self, request):
        """
        Deactivate the current user's account.
        """
        user = request.user
        user.is_active = False
        user.save()
        return Response({'message': 'Account deactivated successfully.'})
    
    @action(detail=True, methods=['post'])
    def approve_teacher(self, request, pk=None):
        """
        Admin approves a teacher account.
        """
        user = self.get_object()
        if user.role != 'teacher':
            return Response(
                {'error': 'User is not a teacher.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user.is_teacher_approved = True
        user.save()
        create_notification.delay(
            user.id, 'teacher_approved', 'You are approved!',
            'Your tutor account has been approved. You are now visible to students.',
        )
        return Response({'message': 'Teacher approved successfully.'})