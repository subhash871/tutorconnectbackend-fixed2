from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.students.models import StudentProfile, StudentPreference
from apps.students.serializers import StudentProfileSerializer, StudentPreferenceSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    serializer_class = StudentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudentProfile.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get', 'put', 'patch'])
    def my_profile(self, request):
        profile, created = StudentProfile.objects.get_or_create(user=request.user)
        if request.method == 'GET':
            serializer = StudentProfileSerializer(profile)
            return Response(serializer.data)
        serializer = StudentProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class StudentPreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = StudentPreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudentPreference.objects.filter(student__user=self.request.user)

    def perform_create(self, serializer):
        student, _ = StudentProfile.objects.get_or_create(user=self.request.user)
        serializer.save(student=student)