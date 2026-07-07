from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.teachers.views import (
    SubjectViewSet, LanguageViewSet, TeacherProfileViewSet,
    QualificationViewSet, ExperienceViewSet, CertificateViewSet,
    TeacherGalleryViewSet, AvailabilityCalendarViewSet
)

app_name = 'teachers'

router = DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'profiles', TeacherProfileViewSet, basename='teacher-profile')
router.register(r'qualifications', QualificationViewSet, basename='qualification')
router.register(r'experiences', ExperienceViewSet, basename='experience')
router.register(r'certificates', CertificateViewSet, basename='certificate')
router.register(r'gallery', TeacherGalleryViewSet, basename='gallery')
router.register(r'availability', AvailabilityCalendarViewSet, basename='availability')

urlpatterns = [
    path('', include(router.urls)),
]