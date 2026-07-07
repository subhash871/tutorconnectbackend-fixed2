from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel
from apps.common.utils import generate_reference_id


class Booking(TimeStampedModel):
    """
    Booking model for student-teacher sessions.
    """

    class BookingStatus(models.TextChoices):
        PENDING = 'pending', _('Pending')
        ACCEPTED = 'accepted', _('Accepted')
        REJECTED = 'rejected', _('Rejected')
        CANCELLED = 'cancelled', _('Cancelled')
        COMPLETED = 'completed', _('Completed')
        RESCHEDULED = 'rescheduled', _('Rescheduled')
        IN_PROGRESS = 'in_progress', _('In Progress')

    class TeachingMode(models.TextChoices):
        HOME_TUITION = 'home_tuition', _('Home Tuition')
        ONLINE_TUITION = 'online_tuition', _('Online Tuition')

    booking_id = models.CharField(
        _('booking ID'),
        max_length=50,
        unique=True,
        default=generate_reference_id,
        editable=False,
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bookings_as_student',
    )
    teacher = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='bookings_as_teacher',
    )
    teacher_profile = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name='bookings',
    )
    subject = models.ForeignKey(
        'teachers.Subject',
        on_delete=models.SET_NULL,
        null=True,
        related_name='bookings',
    )
    status = models.CharField(
        _('status'),
        max_length=20,
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING,
    )
    teaching_mode = models.CharField(
        _('teaching mode'),
        max_length=20,
        choices=TeachingMode.choices,
    )
    
    # Schedule
    preferred_date = models.DateField(_('preferred date'))
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    duration_hours = models.DecimalField(
        _('duration (hours)'),
        max_digits=4,
        decimal_places=2,
    )
    
    # Location / Meeting
    location = models.CharField(
        _('location'),
        max_length=500,
        null=True,
        blank=True,
        help_text=_('Physical address for home tuition'),
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
    )
    meeting_link = models.URLField(
        _('meeting link'),
        max_length=500,
        null=True,
        blank=True,
        help_text=_('Online meeting link for online tuition'),
    )
    
    # Pricing
    hourly_rate = models.DecimalField(
        _('hourly rate'),
        max_digits=10,
        decimal_places=2,
    )
    total_amount = models.DecimalField(
        _('total amount'),
        max_digits=10,
        decimal_places=2,
    )
    is_paid = models.BooleanField(_('paid'), default=False)
    
    # Notes
    student_notes = models.TextField(
        _('student notes'),
        max_length=2000,
        null=True,
        blank=True,
    )
    teacher_notes = models.TextField(
        _('teacher notes'),
        max_length=2000,
        null=True,
        blank=True,
    )
    cancellation_reason = models.TextField(
        _('cancellation reason'),
        max_length=1000,
        null=True,
        blank=True,
    )
    reschedule_count = models.PositiveIntegerField(default=0)
    
    # Timestamps
    accepted_at = models.DateTimeField(null=True, blank=True)
    rejected_at = models.DateTimeField(null=True, blank=True)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    rescheduled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('booking')
        verbose_name_plural = _('bookings')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['student', 'status']),
            models.Index(fields=['teacher', 'status']),
            models.Index(fields=['booking_id']),
            models.Index(fields=['preferred_date']),
        ]

    def __str__(self):
        return f'{self.booking_id} - {self.student.email} with {self.teacher.email}'


class RescheduleRequest(models.Model):
    """
    Request to reschedule a booking.
    """
    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name='reschedule_requests',
    )
    requested_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
    )
    new_date = models.DateField(_('new date'))
    new_start_time = models.TimeField(_('new start time'))
    new_end_time = models.TimeField(_('new end time'))
    reason = models.TextField(_('reason'), max_length=1000)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('reschedule request')
        verbose_name_plural = _('reschedule requests')
        ordering = ['-created_at']