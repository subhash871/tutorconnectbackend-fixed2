from rest_framework import serializers
from apps.users.models import User, OTP, LoginHistory


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'first_name', 'last_name', 'full_name',
            'phone_number', 'role', 'profile_image', 'is_verified',
            'is_phone_verified', 'is_teacher_approved', 'bio', 'address',
            'city', 'state', 'country', 'date_of_birth', 'date_joined',
            'last_login', 'is_active',
        ]
        read_only_fields = ['id', 'is_verified', 'is_phone_verified', 
                           'is_teacher_approved', 'date_joined', 'last_login']

    def get_full_name(self, obj):
        return obj.get_full_name()


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile updates.
    """
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'phone_number', 'profile_image',
            'bio', 'address', 'city', 'state', 'country', 'date_of_birth',
        ]


class UserListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for listing users.
    """
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'full_name', 'profile_image', 
                 'role', 'is_verified', 'city', 'country']
    
    def get_full_name(self, obj):
        return obj.get_full_name()


class OTPSerializer(serializers.ModelSerializer):
    """
    Serializer for OTP model.
    """
    class Meta:
        model = OTP
        fields = ['id', 'user', 'otp', 'purpose', 'is_used', 'created_at', 'expires_at']
        read_only_fields = ['id', 'created_at', 'expires_at']


class LoginHistorySerializer(serializers.ModelSerializer):
    """
    Serializer for login history.
    """
    class Meta:
        model = LoginHistory
        fields = ['id', 'ip_address', 'user_agent', 'device_type', 
                 'location', 'is_successful', 'login_time']
        read_only_fields = ['id', 'login_time']