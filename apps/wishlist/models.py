from django.db import models
from django.utils.translation import gettext_lazy as _


class Wishlist(models.Model):
    """
    Wishlist model for students to save teachers.
    """
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='wishlist',
    )
    teacher = models.ForeignKey(
        'teachers.TeacherProfile',
        on_delete=models.CASCADE,
        related_name='wishlisted_by',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('wishlist')
        verbose_name_plural = _('wishlists')
        unique_together = ['student', 'teacher']
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.student.get_full_name()} - {self.teacher}'