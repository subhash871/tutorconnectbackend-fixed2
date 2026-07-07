try:
    from celery import shared_task
except ImportError:
    class _SyncTask:
        def __init__(self, func, bind=False):
            self.func = func
            self.bind = bind

        def __call__(self, *args, **kwargs):
            if self.bind:
                return self.func(self, *args, **kwargs)
            return self.func(*args, **kwargs)

        def delay(self, *args, **kwargs):
            return self(*args, **kwargs)

        apply_async = delay

        def retry(self, exc=None, countdown=None):
            if exc:
                raise exc
            raise RuntimeError('Task retry requested, but Celery is not installed.')

    def shared_task(*decorator_args, **decorator_kwargs):
        bind = decorator_kwargs.get('bind', False)

        if decorator_args and callable(decorator_args[0]):
            return _SyncTask(decorator_args[0], bind=bind)

        def decorator(func):
            return _SyncTask(func, bind=bind)

        return decorator
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from apps.notifications.models import Notification, EmailLog


@shared_task
def send_email_verification(user_id, otp):
    """Send email verification OTP."""
    from apps.users.models import User
    user = User.objects.get(id=user_id)
    subject = 'Verify your email - TutorConnect Nepal'
    message = f'Your verification OTP is: {otp}\nThis OTP expires in 10 minutes.'
    send_email_task.delay(user.email, subject, message)


@shared_task
def send_password_reset_email(user_id, otp):
    """Send password reset OTP."""
    from apps.users.models import User
    user = User.objects.get(id=user_id)
    subject = 'Password Reset - TutorConnect Nepal'
    message = f'Your password reset OTP is: {otp}\nThis OTP expires in 10 minutes.'
    send_email_task.delay(user.email, subject, message)


@shared_task
def send_otp_email(user_id, otp, purpose):
    """Send OTP email for various purposes."""
    from apps.users.models import User
    user = User.objects.get(id=user_id)
    subject = f'OTP for {purpose.replace("_", " ")} - TutorConnect Nepal'
    message = f'Your OTP is: {otp}\nThis OTP expires in 10 minutes.'
    send_email_task.delay(user.email, subject, message)


@shared_task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, message):
    """Generic email sending task."""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
        EmailLog.objects.create(
            recipient=recipient,
            subject=subject,
            body=message,
            is_sent=True,
            sent_at=timezone.now(),
        )
    except Exception as e:
        EmailLog.objects.create(
            recipient=recipient,
            subject=subject,
            body=message,
            is_sent=False,
            error_message=str(e),
        )
        raise self.retry(exc=e, countdown=60)


@shared_task
def create_notification(recipient_id, notification_type, title, message, data=None):
    """Create an in-app notification."""
    from apps.users.models import User
    try:
        recipient = User.objects.get(id=recipient_id)
        Notification.objects.create(
            recipient=recipient,
            notification_type=notification_type,
            title=title,
            message=message,
            data=data,
        )
    except User.DoesNotExist:
        pass


@shared_task
def send_booking_reminder(booking_id):
    """Send booking reminder to both student and teacher."""
    from apps.bookings.models import Booking
    try:
        booking = Booking.objects.get(id=booking_id)
        student_message = f'You have a session with {booking.teacher.get_full_name()} tomorrow.'
        create_notification.delay(
            booking.student.id, 'reminder', 'Booking Reminder', student_message
        )
        teacher_message = f'You have a session with {booking.student.get_full_name()} tomorrow.'
        create_notification.delay(
            booking.teacher.id, 'reminder', 'Booking Reminder', teacher_message
        )
    except Booking.DoesNotExist:
        pass
