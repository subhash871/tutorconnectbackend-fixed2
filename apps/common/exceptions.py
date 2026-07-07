from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF that provides consistent error responses.
    """
    # Call DRF's default exception handler first
    response = exception_handler(exc, context)
    
    if response is not None:
        # Customize the response format
        custom_response_data = {
            'success': False,
            'error': {
                'message': str(exc),
                'details': response.data,
                'status_code': response.status_code
            }
        }
        response.data = custom_response_data
    else:
        # Handle unexpected exceptions
        logger.error(f'Unhandled exception: {exc}', exc_info=True)
        custom_response_data = {
            'success': False,
            'error': {
                'message': 'An unexpected error occurred.',
                'details': str(exc),
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
        }
        response = Response(custom_response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return response


class APIException(Exception):
    """
    Base API Exception class.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A server error occurred.'
    default_code = 'error'

    def __init__(self, detail=None, status_code=None):
        if detail is None:
            detail = self.default_detail
        if status_code is not None:
            self.status_code = status_code
        
        self.detail = detail
        super().__init__(detail)


class ValidationError(APIException):
    """
    Custom validation error.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid data provided.'
    default_code = 'invalid'


class AuthenticationError(APIException):
    """
    Custom authentication error.
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = 'Authentication credentials were not provided.'
    default_code = 'authentication_error'


class PermissionDenied(APIException):
    """
    Custom permission denied error.
    """
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'You do not have permission to perform this action.'
    default_code = 'permission_denied'


class NotFound(APIException):
    """
    Custom not found error.
    """
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Resource not found.'
    default_code = 'not_found'


class Throttled(APIException):
    """
    Custom throttled error.
    """
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = 'Request was throttled.'
    default_code = 'throttled'