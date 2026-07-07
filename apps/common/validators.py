import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator:
    """
    Validator for Nepali phone numbers.
    Accepts formats: 98xxxxxxxx, 97xxxxxxxx, +97798xxxxxxxx
    """
    def __init__(self, message=None):
        self.message = message or _('Enter a valid Nepali phone number.')
        self.code = 'invalid_phone_number'
        
    def __call__(self, value):
        pattern = re.compile(r'^(\+977)?[9][6-8][0-9]{8}$')
        if not pattern.match(value):
            raise ValidationError(
                self.message,
                code=self.code
            )
    
    def __eq__(self, other):
        return isinstance(other, PhoneNumberValidator)


class PasswordStrengthValidator:
    """
    Validator to ensure password has minimum strength.
    """
    def __init__(self, message=None):
        pass
        
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _('Password must be at least 8 characters long.'),
                code='password_too_short'
            )
        
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _('Password must contain at least one digit.'),
                code='password_no_digit'
            )
        
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                _('Password must contain at least one letter.'),
                code='password_no_letter'
            )
        
        if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?' for char in password):
            raise ValidationError(
                _('Password must contain at least one special character.'),
                code='password_no_special'
            )


class RatingValidator:
    """
    Validator for rating values (1-5).
    """
    def __init__(self, message=None):
        self.message = message or _('Rating must be between 1 and 5.')
        self.code = 'invalid_rating'
        
    def __call__(self, value):
        if value < 1 or value > 5:
            raise ValidationError(
                self.message,
                code=self.code
            )
    
    def __eq__(self, other):
        return isinstance(other, RatingValidator)


class LatitudeValidator:
    """
    Validator for latitude values (-90 to 90).
    """
    def __init__(self, message=None):
        self.message = message or _('Latitude must be between -90 and 90.')
        self.code = 'invalid_latitude'
        
    def __call__(self, value):
        if value < -90 or value > 90:
            raise ValidationError(
                self.message,
                code=self.code
            )
    
    def __eq__(self, other):
        return isinstance(other, LatitudeValidator)


class LongitudeValidator:
    """
    Validator for longitude values (-180 to 180).
    """
    def __init__(self, message=None):
        self.message = message or _('Longitude must be between -180 and 180.')
        self.code = 'invalid_longitude'
        
    def __call__(self, value):
        if value < -180 or value > 180:
            raise ValidationError(
                self.message,
                code=self.code
            )
    
    def __eq__(self, other):
        return isinstance(other, LongitudeValidator)


class HourlyRateValidator:
    """
    Validator for hourly rate (must be positive).
    """
    def __init__(self, message=None):
        self.message = message or _('Hourly rate must be greater than 0.')
        self.code = 'invalid_hourly_rate'
        
    def __call__(self, value):
        if value <= 0:
            raise ValidationError(
                self.message,
                code=self.code
            )
    
    def __eq__(self, other):
        return isinstance(other, HourlyRateValidator)