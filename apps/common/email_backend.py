from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from datetime import timedelta

from apps.authentication.serializers import (
    RegisterSerializer, LoginSerializer, TokenSerializer,
    ChangePasswordSerializer, ForgotPasswordSerializer,
    ResetPasswordSerializer, EmailVerificationSerializer,
    OTPVerificationSerializer, ResendOTPSerializer, GoogleAuthSerializer
)
from apps.users.models import User, OTP
from apps.users.serializers import UserSerializer
from apps.users.services import UserService, OTPService, LoginHistoryService
from apps.common.utils import generate_otp


def get_tokens_for_user(user):
    """Generate JWT tokens for a user."""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register a new user."""
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    
    # Generate OTP for email verification
    otp = OTPService.generate_otp(user, 'email_verification')
    
    # Send verification email (async task)
    from apps.notifications.tasks import send_email_verification
    send_email_verification.delay(user.id, otp.otp)
    
    return Response({
        'success': True,
        'message': 'Registration successful. Please verify your email with the OTP sent to you.',
        'data': {
            'user': UserSerializer(user).data,
        }
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Authenticate user and return JWT tokens."""
    serializer = LoginSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    
    # Record login history
    LoginHistoryService.record_login(user, request, is_successful=True)
    
    tokens = get_tokens_for_user(user)
    
    return Response({
        'success': True,
        'message': 'Login successful.',
        'data': {
            'user': UserSerializer(user).data,
            'tokens': tokens,
        }
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """Refresh JWT access token."""
    from rest_framework_simplejwt.tokens import RefreshToken
    refresh = request.data.get('refresh')
    
    if not refresh:
        return Response({
            'success': False,
            'error': 'Refresh token is required.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        token = RefreshToken(refresh)
        return Response({
            'success': True,
            'data': {
                'access': str(token.access_token),
            }
        })
    except Exception as e:
        return Response({
            'success': False,
            'error': 'Invalid or expired refresh token.'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Logout user and blacklist refresh token."""
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        
        logout(request)
        
        return Response({
            'success': True,
            'message': 'Logout successful.'
        })
    except Exception as e:
        return Response({
            'success': False,
            'error': 'Logout failed.'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    """Change user password."""
    serializer = ChangePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    user = request.user
    
    if not user.check_password(serializer.validated_data['old_password']):
        return Response({
            'success': False,
            'error': 'Current password is incorrect.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user.set_password(serializer.validated_data['new_password'])
    user.save()
    
    return Response({
        'success': True,
        'message': 'Password changed successfully.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def forgot_password(request):
    """Send OTP for password reset."""
    serializer = ForgotPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    user = User.objects.get(email__iexact=email)
    
    # Generate OTP
    otp = OTPService.generate_otp(user, 'password_reset')
    
    # Send password reset email (async task)
    from apps.notifications.tasks import send_password_reset_email
    send_password_reset_email.delay(user.id, otp.otp)
    
    return Response({
        'success': True,
        'message': 'Password reset OTP sent to your email.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def reset_password(request):
    """Reset password using OTP."""
    serializer = ResetPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    otp_code = serializer.validated_data['otp']
    new_password = serializer.validated_data['new_password']
    
    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return Response({
            'success': False,
            'error': 'User not found.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    # Verify OTP
    if not OTPService.verify_otp(user, otp_code, 'password_reset'):
        return Response({
            'success': False,
            'error': 'Invalid or expired OTP.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user.set_password(new_password)
    user.save()
    
    return Response({
        'success': True,
        'message': 'Password reset successful.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email(request):
    """Verify email using OTP."""
    serializer = EmailVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    otp_code = serializer.validated_data['otp']
    
    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return Response({
            'success': False,
            'error': 'User not found.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if not OTPService.verify_otp(user, otp_code, 'email_verification'):
        return Response({
            'success': False,
            'error': 'Invalid or expired OTP.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user.is_verified = True
    user.save(update_fields=['is_verified'])
    
    return Response({
        'success': True,
        'message': 'Email verified successfully.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    """Verify OTP for any purpose."""
    serializer = OTPVerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    otp_code = serializer.validated_data['otp']
    purpose = serializer.validated_data['purpose']
    
    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return Response({
            'success': False,
            'error': 'User not found.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    if not OTPService.verify_otp(user, otp_code, purpose):
        return Response({
            'success': False,
            'error': 'Invalid or expired OTP.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if purpose == 'email_verification':
        user.is_verified = True
        user.save(update_fields=['is_verified'])
    
    return Response({
        'success': True,
        'message': 'OTP verified successfully.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def resend_otp(request):
    """Resend OTP."""
    serializer = ResendOTPSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    email = serializer.validated_data['email']
    purpose = serializer.validated_data['purpose']
    
    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return Response({
            'success': False,
            'error': 'User not found.'
        }, status=status.HTTP_404_NOT_FOUND)
    
    otp = OTPService.generate_otp(user, purpose)
    
    # Send OTP via email (async task)
    from apps.notifications.tasks import send_otp_email
    send_otp_email.delay(user.id, otp.otp, purpose)
    
    return Response({
        'success': True,
        'message': 'OTP resent successfully.'
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def google_auth(request):
    """Authenticate (or register) a user using a Google-issued ID token."""
    serializer = GoogleAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    id_token_str = serializer.validated_data['id_token']

    from django.conf import settings

    if not getattr(settings, 'GOOGLE_CLIENT_ID', ''):
        return Response({
            'success': False,
            'error': 'Google sign-in is not configured on this server.',
        }, status=status.HTTP_501_NOT_IMPLEMENTED)

    try:
        from google.oauth2 import id_token as google_id_token
        from google.auth.transport import requests as google_requests

        idinfo = google_id_token.verify_oauth2_token(
            id_token_str, google_requests.Request(), settings.GOOGLE_CLIENT_ID,
        )
    except Exception:
        return Response({
            'success': False,
            'error': 'Invalid or expired Google token.',
        }, status=status.HTTP_401_UNAUTHORIZED)

    email = idinfo.get('email')
    if not email or not idinfo.get('email_verified'):
        return Response({
            'success': False,
            'error': "Google account has no verified email.",
        }, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(email=email).first()
    created = False
    if not user:
        base_username = email.split('@')[0]
        username = base_username
        suffix = 1
        while User.objects.filter(username=username).exists():
            suffix += 1
            username = f'{base_username}{suffix}'

        user = UserService.create_user(
            email=email,
            username=username,
            password=None,
            role=request.data.get('role', 'student'),
            first_name=idinfo.get('given_name', ''),
            last_name=idinfo.get('family_name', ''),
            is_verified=True,
        )
        created = True

    tokens = get_tokens_for_user(user)
    LoginHistoryService.record_login(user, request, is_successful=True)

    return Response({
        'success': True,
        'message': 'Account created and signed in with Google.' if created else 'Signed in with Google.',
        'data': {
            'user': UserSerializer(user).data,
            'tokens': tokens,
            'created': created,
        },
    })