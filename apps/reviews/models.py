from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class Review(TimeStampedModel):
    """
    Review model for student reviews of teachers.
    """
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='reviews_given',
    )
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    booking = models.ForeignKey(
        'bookings.Booking',
        on_delete=models.SET_NULL,
        null=True,
        related_name='reviews',
    )
    rating = models.PositiveSmallIntegerField(
        _('rating'),
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    comment = models.TextField(_('comment'), max_length=2000, null=True, blank=True)
    is_approved = models.BooleanField(_('approved'), default=True)

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
        unique_together = ['student', 'teacher']
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['teacher', 'rating']),
        ]

    def __str__(self):
        return f'{self.student.get_full_name()} - {self.teacher} ({self.rating}/5)'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.teacher.update_rating()