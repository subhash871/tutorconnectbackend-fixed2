from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from apps.users.models import User, OTP, LoginHistory


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom User admin for TutorConnect Nepal.
    """
    list_display = ['email', 'username', 'role', 'is_verified', 'is_teacher_approved', 'is_active', 'date_joined']
    list_filter = ['role', 'is_verified', 'is_teacher_approved', 'is_active', 'country']
    search_fields = ['email', 'username', 'phone_number', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'profile_image')}),
        (_('Address'), {'fields': ('address', 'city', 'state', 'country')}),
        (_('Role & Status'), {'fields': ('role', 'is_verified', 'is_phone_verified', 'is_teacher_approved', 'bio')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['user', 'purpose', 'is_used', 'created_at', 'expires_at']
    list_filter = ['purpose', 'is_used']
    search_fields = ['user__email', 'user__username', 'otp']
    ordering = ['-created_at']


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip_address', 'device_type', 'is_successful', 'login_time']
    list_filter = ['is_successful', 'device_type']
    search_fields = ['user__email', 'ip_address']
    ordering = ['-login_time']