from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.wishlist.models import Wishlist
from apps.wishlist.serializers import WishlistSerializer
from apps.common.permissions import IsStudent


class WishlistViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated, IsStudent]

    def get_queryset(self):
        return Wishlist.objects.filter(student=self.request.user).select_related(
            'teacher__user', 'teacher'
        ).prefetch_related('teacher__subjects')

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    @action(detail=False, methods=['delete'])
    def clear(self, request):
        self.get_queryset().delete()
        return Response({'message': 'Wishlist cleared.'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'])
    def check(self, request):
        teacher_id = request.query_params.get('teacher_id')
        if not teacher_id:
            return Response({'error': 'teacher_id is required.'}, status=400)
        exists = self.get_queryset().filter(teacher_id=teacher_id).exists()
        return Response({'is_wishlisted': exists})