from django.utils import timezone
from django.db import transaction
from datetime import timedelta
from apps.users.models import User, OTP, LoginHistory
from apps.common.utils import generate_otp, get_client_ip


class UserService:
    """
    Service layer for user-related business logic.
    """
    
    @staticmethod
    @transaction.atomic
    def create_user(email, username, password, role='student', **extra_fields):
        """
        Create a new user with the given parameters.
        """
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            role=role,
            **extra_fields
        )
        return user
    
    @staticmethod
    @transaction.atomic
    def update_user_profile(user, data):
        """
        Update user profile fields.
        """
        for field in ['first_name', 'last_name', 'phone_number', 'bio', 
                      'address', 'city', 'state', 'country', 'date_of_birth']:
            if field in data:
                setattr(user, field, data[field])
        
        if 'profile_image' in data:
            user.profile_image = data['profile_image']
        
        user.save()
        return user
    
    @staticmethod
    def deactivate_user(user):
        """Deactivate a user account."""
        user.is_active = False
        user.save()
        return user
    
    @staticmethod
    def activate_user(user):
        """Activate a user account."""
        user.is_active = True
        user.save()
        return user


class OTPService:
    """
    Service layer for OTP operations.
    """
    
    @staticmethod
    @transaction.atomic
    def generate_otp(user, purpose, expiry_minutes=10):
        """
        Generate and save an OTP for a user.
        """
        otp_code = generate_otp()
        otp = OTP.objects.create(
            user=user,
            otp=otp_code,
            purpose=purpose,
            expires_at=timezone.now() + timedelta(minutes=expiry_minutes)
        )
        return otp
    
    @staticmethod
    def verify_otp(user, otp_code, purpose):
        """
        Verify an OTP for a user.
        """
        otp = OTP.objects.filter(
            user=user,
            otp=otp_code,
            purpose=purpose,
            is_used=False
        ).first()
        
        if not otp:
            return False
        
        if otp.is_expired:
            return False
        
        otp.is_used = True
        otp.save()
        return True


class LoginHistoryService:
    """
    Service layer for login history operations.
    """
    
    @staticmethod
    def record_login(user, request, is_successful=True):
        """
        Record a login attempt.
        """
        LoginHistory.objects.create(
            user=user,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            is_successful=is_successful,
        )