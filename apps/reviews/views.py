from rest_framework import viewsets, permissions
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer, ReviewCreateSerializer
from apps.common.permissions import IsStudent
from apps.notifications.tasks import create_notification


class IsReviewOwnerOrReadOnly(permissions.BasePermission):
    """Only the student who wrote a review may update or delete it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.student_id == request.user.id


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('student', 'teacher__user').all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated(), IsStudent()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsReviewOwnerOrReadOnly()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        review = serializer.save()
        create_notification.delay(
            review.teacher.user_id, 'new_review', 'New review',
            f'{review.student.get_full_name()} left you a {review.rating}-star review.',
            {'review_id': review.id, 'teacher_id': review.teacher_id},
        )

    def get_queryset(self):
        user = self.request.user
        if self.action == 'list':
            teacher_id = self.request.query_params.get('teacher')
            qs = self.queryset.filter(is_approved=True)
            if teacher_id:
                qs = qs.filter(teacher_id=teacher_id)
            return qs
        if self.action in ['update', 'partial_update', 'destroy']:
            # A student can only ever reach their own rows here; combined with
            # IsReviewOwnerOrReadOnly this is defense in depth, not the only check.
            if user.is_authenticated and user.role != 'admin':
                return self.queryset.filter(student=user)
        return self.queryset
