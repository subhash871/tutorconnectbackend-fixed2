from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
 
    """
    Custom User model for TutorConnect Nepal.
    Supports Student, Teacher, and Admin roles.
    """

    class Role(models.TextChoices):
        STUDENT = 'student', _('Student')
        TEACHER = 'teacher', _('Teacher')
        ADMIN = 'admin', _('Admin')

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(
        _('phone number'),
        max_length=15,
        unique=True,
        null=True,
        blank=True,
    )
    role = models.CharField(
        _('role'),
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )
    profile_image = models.FileField(
        _('profile image'),
        upload_to='profiles/',
        null=True,
        blank=True,
    )
    is_verified = models.BooleanField(
        _('verified'),
        default=False,
        help_text=_('Designates whether the user has verified their email/phone.'),
    )
    is_phone_verified = models.BooleanField(
        _('phone verified'),
        default=False,
    )
    is_teacher_approved = models.BooleanField(
        _('teacher approved'),
        default=False,
        help_text=_('Designates whether the teacher profile has been approved by admin.'),
    )
    date_of_birth = models.DateField(
        _('date of birth'),
        null=True,
        blank=True,
    )
    address = models.TextField(
        _('address'),
        max_length=500,
        null=True,
        blank=True,
    )
    city = models.CharField(
        _('city'),
        max_length=100,
        null=True,
        blank=True,
    )
    state = models.CharField(
        _('state'),
        max_length=100,
        null=True,
        blank=True,
    )
    country = models.CharField(
        _('country'),
        max_length=100,
        default='Nepal',
    )
    bio = models.TextField(
        _('bio'),
        max_length=1000,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Override groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set',
        related_query_name='custom_user',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['role']),
            models.Index(fields=['is_verified']),
            models.Index(fields=['is_teacher_approved']),
        ]

    def __str__(self):
        return f'{self.get_full_name() or self.email} ({self.get_role_display()})'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]

    @property
    def is_student(self):
        return self.role == self.Role.STUDENT

    @property
    def is_teacher(self):
        return self.role == self.Role.TEACHER

    @property
    def is_admin_user(self):
        return self.role == self.Role.ADMIN or self.is_superuser


class OTP(models.Model):
    """
    OTP model for email and phone verification.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='otps',
    )
    otp = models.CharField(max_length=6)
    purpose = models.CharField(
        max_length=20,
        choices=[
            ('email_verification', 'Email Verification'),
            ('phone_verification', 'Phone Verification'),
            ('password_reset', 'Password Reset'),
        ],
    )
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        verbose_name = _('OTP')
        verbose_name_plural = _('OTPs')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'purpose']),
            models.Index(fields=['otp']),
        ]

    def __str__(self):
        return f'{self.user.email} - {self.purpose}'

    @property
    def is_expired(self):
        from django.utils import timezone
        return timezone.now() > self.expires_at


class LoginHistory(models.Model):
    """
    Track user login history for security.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='login_history',
    )
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_successful = models.BooleanField(default=True)
    login_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('login history')
        verbose_name_plural = _('login histories')
        ordering = ['-login_time']
        indexes = [
            models.Index(fields=['user', '-login_time']),
        ]

    def __str__(self):
        return f'{self.user.email} - {self.login_time}'