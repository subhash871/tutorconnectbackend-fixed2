from rest_framework import viewsets, status, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Avg
from apps.teachers.models import (
    TeacherProfile, Subject, Language, Qualification,
    Experience, Certificate, TeacherGallery, AvailabilityCalendar,
    TeacherAvailability
)
from apps.teachers.serializers import (
    SubjectSerializer, LanguageSerializer, QualificationSerializer,
    ExperienceSerializer, CertificateSerializer, TeacherGallerySerializer,
    AvailabilityCalendarSerializer, TeacherAvailabilitySerializer,
    TeacherProfileListSerializer, TeacherProfileDetailSerializer,
    TeacherProfileCreateSerializer
)
from apps.teachers.filters import TeacherFilter
from apps.common.permissions import IsTeacher, IsAdmin
from apps.common.pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.filter(is_active=True)
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name']
    ordering_fields = ['name']


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['name']


class TeacherProfileViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing teacher profiles.
    """
    queryset = TeacherProfile.objects.select_related('user').prefetch_related(
        'subjects', 'languages', 'qualifications', 'experiences',
        'certificates', 'gallery_images', 'availability'
    )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TeacherFilter
    search_fields = ['user__first_name', 'user__last_name', 'headline', 'about', 'location']
    ordering_fields = ['hourly_rate', 'average_rating', 'years_of_experience', 'total_reviews', 'created_at']
    pagination_class = StandardResultsSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return TeacherProfileListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return TeacherProfileCreateSerializer
        return TeacherProfileDetailSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsTeacher]
        else:
            permission_classes = [IsAuthenticated]
        return [p() for p in permission_classes]

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user

        if self.action == 'list':
            # Show only verified, approved, and available teachers for listing
            return queryset.filter(
                user__is_verified=True,
                user__is_teacher_approved=True,
                is_available=True,
                user__is_active=True
            )
        
        if self.action == 'retrieve':
            return queryset

        # For update/delete, only own profile
        return queryset.filter(user=user)

    @action(detail=False, methods=['get', 'put', 'patch'])
    def my_profile(self, request):
        """Get or update the current teacher's profile."""
        profile = TeacherProfile.objects.select_related('user').prefetch_related(
            'subjects', 'languages', 'qualifications', 'experiences',
            'certificates', 'gallery_images', 'availability'
        ).filter(user=request.user).first()

        if not profile:
            return Response(
                {'error': 'Teacher profile not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.method == 'GET':
            serializer = TeacherProfileDetailSerializer(profile)
            return Response(serializer.data)

        serializer = TeacherProfileCreateSerializer(
            profile, data=request.data, partial=True, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(TeacherProfileDetailSerializer(profile).data)

    @action(detail=True, methods=['post'])
    def add_subject(self, request, pk=None):
        """Add a subject to the teacher's profile."""
        profile = self.get_object()
        subject_id = request.data.get('subject_id')
        try:
            subject = Subject.objects.get(id=subject_id)
            profile.subjects.add(subject)
            return Response({'message': 'Subject added successfully.'})
        except Subject.DoesNotExist:
            return Response(
                {'error': 'Subject not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['post'])
    def remove_subject(self, request, pk=None):
        """Remove a subject from the teacher's profile."""
        profile = self.get_object()
        subject_id = request.data.get('subject_id')
        try:
            subject = Subject.objects.get(id=subject_id)
            profile.subjects.remove(subject)
            return Response({'message': 'Subject removed successfully.'})
        except Subject.DoesNotExist:
            return Response(
                {'error': 'Subject not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=['post'])
    def toggle_availability(self, request, pk=None):
        """Toggle teacher availability status."""
        profile = self.get_object()
        profile.is_available = not profile.is_available
        profile.save(update_fields=['is_available'])
        return Response({
            'is_available': profile.is_available,
            'message': f"Availability set to {'available' if profile.is_available else 'unavailable'}"
        })


class QualificationViewSet(viewsets.ModelViewSet):
    serializer_class = QualificationSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        return Qualification.objects.filter(teacher__user=self.request.user)

    def perform_create(self, serializer):
        profile = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        return Experience.objects.filter(teacher__user=self.request.user)

    def perform_create(self, serializer):
        profile = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        return Certificate.objects.filter(teacher__user=self.request.user)

    def perform_create(self, serializer):
        profile = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)


class TeacherGalleryViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherGallerySerializer
    permission_classes = [IsAuthenticated, IsTeacher]

    def get_queryset(self):
        return TeacherGallery.objects.filter(teacher__user=self.request.user)

    def perform_create(self, serializer):
        profile = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)


class AvailabilityCalendarViewSet(viewsets.ModelViewSet):
    serializer_class = AvailabilityCalendarSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsTeacher]
        return [p() for p in permission_classes]

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            queryset = AvailabilityCalendar.objects.all()
            teacher_id = self.request.query_params.get('teacher') or self.request.query_params.get('teacher_id')
            if teacher_id:
                queryset = queryset.filter(teacher_id=teacher_id)
            return queryset
        # Write actions: teachers can only see/modify their own availability
        return AvailabilityCalendar.objects.filter(teacher__user=self.request.user)

    def perform_create(self, serializer):
        profile = TeacherProfile.objects.get(user=self.request.user)
        serializer.save(teacher=profile)