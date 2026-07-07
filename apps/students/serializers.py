from rest_framework import serializers
from apps.students.models import StudentProfile, StudentPreference
from apps.users.serializers import UserSerializer


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'grade_level', 'school', 'parent_name', 'parent_phone',
                 'parent_email', 'learning_goals', 'preferred_mode', 'max_budget',
                 'total_bookings', 'total_hours_learned', 'created_at', 'updated_at']
        read_only_fields = ['id', 'total_bookings', 'total_hours_learned', 'created_at', 'updated_at']


class StudentPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPreference
        fields = ['id', 'subject', 'preferred_gender', 'preferred_experience']