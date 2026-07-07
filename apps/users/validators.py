from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_email_unique(email):
    """Validate that email is unique."""
    from apps.users.models import User
    if User.objects.filter(email__iexact=email).exists():
        raise ValidationError(_('A user with this email already exists.'))


def validate_username_unique(username):
    """Validate that username is unique."""
    from apps.users.models import User
    if User.objects.filter(username__iexact=username).exists():
        raise ValidationError(_('A user with this username already exists.'))


def validate_phone_unique(phone_number):
    """Validate that phone number is unique."""
    from apps.users.models import User
    if phone_number and User.objects.filter(phone_number=phone_number).exists():
        raise ValidationError(_('A user with this phone number already exists.'))