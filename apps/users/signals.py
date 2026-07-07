from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from apps.users.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to create related profiles when a user is created.
    """
    if created:
        if instance.role == 'student':
            from apps.students.models import StudentProfile
            StudentProfile.objects.get_or_create(user=instance)
        elif instance.role == 'teacher':
            from apps.teachers.models import TeacherProfile
            # Created unavailable/unverified with placeholder values so it
            # never appears publicly until the teacher fills in real details
            # (via PATCH /teachers/profiles/my_profile/) and an admin approves
            # their account.
            TeacherProfile.objects.get_or_create(
                user=instance,
                defaults={'hourly_rate': 0, 'is_available': False},
            )
