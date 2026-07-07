from rest_framework import serializers
from apps.teachers.models import (
    TeacherProfile, Subject, Language, Qualification, 
    Experience, Certificate, TeacherGallery, AvailabilityCalendar,
    TeacherAvailability
)
from apps.users.serializers import UserSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'icon', 'is_active']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'code']


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['id', 'degree', 'institution', 'field_of_study', 'start_year', 
                 'end_year', 'is_current', 'description', 'certificate']
        read_only_fields = ['id']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title', 'organization', 'location', 'start_date', 
                 'end_date', 'is_current', 'description']
        read_only_fields = ['id']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'title', 'issuing_organization', 'credential_id', 
                 'credential_url', 'issue_date', 'expiry_date', 'does_not_expire', 'file']
        read_only_fields = ['id']


class TeacherGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherGallery
        fields = ['id', 'image', 'caption', 'is_primary']
        read_only_fields = ['id']


class AvailabilityCalendarSerializer(serializers.ModelSerializer):
    day_name = serializers.SerializerMethodField()

    class Meta:
        model = AvailabilityCalendar
        fields = ['id', 'day_of_week', 'day_name', 'start_time', 'end_time', 'is_available']
        read_only_fields = ['id']

    def get_day_name(self, obj):
        return obj.get_day_of_week_display()


class TeacherAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAvailability
        fields = ['id', 'date', 'start_time', 'end_time', 'is_available', 'reason']
        read_only_fields = ['id']


class TeacherProfileListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing teachers.
    """
    user = UserSerializer(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = TeacherProfile
        fields = [
            'id', 'user', 'full_name', 'title', 'headline', 'hourly_rate',
            'location', 'teaching_mode', 'average_rating', 'total_reviews',
            'total_students', 'years_of_experience', 'is_verified',
            'is_available', 'subjects', 'profile_image',
        ]
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()


class TeacherProfileDetailSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for teacher profiles.
    """
    user = UserSerializer(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    qualifications = QualificationSerializer(many=True, read_only=True)
    experiences = ExperienceSerializer(many=True, read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    gallery_images = TeacherGallerySerializer(many=True, read_only=True)
    availability = AvailabilityCalendarSerializer(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = TeacherProfile
        fields = [
            'id', 'user', 'full_name', 'title', 'headline', 'about',
            'teaching_mode', 'experience_level', 'years_of_experience',
            'hourly_rate', 'location', 'latitude', 'longitude', 'service_area',
            'meeting_link', 'profile_image', 'demo_video',
            'is_verified', 'verified_at', 'is_available', 'is_featured',
            'total_students', 'total_hours', 'total_bookings',
            'average_rating', 'total_reviews', 'completion_rate', 'response_time',
            'max_students', 'website', 'linkedin', 'youtube',
            'subjects', 'languages', 'qualifications', 'experiences',
            'certificates', 'gallery_images', 'availability',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'is_verified', 'verified_at', 'total_students',
                          'total_hours', 'total_bookings', 'average_rating',
                          'total_reviews', 'completion_rate', 'response_time']

    def get_full_name(self, obj):
        return obj.user.get_full_name()


class TeacherProfileCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating/updating teacher profile.
    """
    class Meta:
        model = TeacherProfile
        fields = [
            'title', 'headline', 'about', 'teaching_mode', 'experience_level',
            'years_of_experience', 'hourly_rate', 'location', 'latitude',
            'longitude', 'service_area', 'meeting_link', 'profile_image',
            'demo_video', 'website', 'linkedin', 'youtube', 'is_available',
            'max_students',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        profile, created = TeacherProfile.objects.get_or_create(
            user=user,
            defaults=validated_data
        )
        if not created:
            for attr, value in validated_data.items():
                setattr(profile, attr, value)
            profile.save()
        return profile