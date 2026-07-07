from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentProfileViewSet, StudentPreferenceViewSet

app_name = 'students'

router = DefaultRouter()
router.register(r'profiles', StudentProfileViewSet, basename='student-profile')
router.register(r'preferences', StudentPreferenceViewSet, basename='student-preference')

urlpatterns = [
    path('', include(router.urls)),
]