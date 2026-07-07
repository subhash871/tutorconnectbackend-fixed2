from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class StudentProfile(TimeStampedModel):
    """
    Extended profile for students.
    """
    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='student_profile',
    )
    grade_level = models.CharField(
        _('grade level'),
        max_length=50,
        null=True,
        blank=True,
    )
    school = models.CharField(
        _('school'),
        max_length=200,
        null=True,
        blank=True,
    )
    parent_name = models.CharField(
        _('parent/guardian name'),
        max_length=200,
        null=True,
        blank=True,
    )
    parent_phone = models.CharField(
        _('parent/guardian phone'),
        max_length=15,
        null=True,
        blank=True,
    )
    parent_email = models.EmailField(
        _('parent/guardian email'),
        null=True,
        blank=True,
    )
    learning_goals = models.TextField(
        _('learning goals'),
        max_length=2000,
        null=True,
        blank=True,
    )
    preferred_mode = models.CharField(
        _('preferred teaching mode'),
        max_length=20,
        choices=[
            ('home_tuition', 'Home Tuition'),
            ('online_tuition', 'Online Tuition'),
            ('both', 'Both'),
        ],
        default='both',
    )
    max_budget = models.DecimalField(
        _('maximum budget per hour'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    total_bookings = models.PositiveIntegerField(default=0)
    total_hours_learned = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('student profile')
        verbose_name_plural = _('student profiles')

    def __str__(self):
        return f'{self.user.get_full_name()} - Student'


class StudentPreference(models.Model):
    """
    Student preferences for teacher matching.
    """
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name='preferences',
    )
    subject = models.ForeignKey(
        'teachers.Subject',
        on_delete=models.CASCADE,
        related_name='student_preferences',
    )
    preferred_gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('any', 'Any')],
        default='any',
    )
    preferred_experience = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('student preference')
        verbose_name_plural = _('student preferences')
        unique_together = ['student', 'subject']