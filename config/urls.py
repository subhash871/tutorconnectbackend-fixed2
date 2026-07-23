import json
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from config.health import health_check

User = get_user_model()


@csrf_exempt
def force_reset_password_view(request):
    """
    TEMPORARY: Force-reset a user's password using FORCE_PASSWORD_RESET_SECRET.
    POST with JSON: { "secret": "...", "email": "...", "new_password": "..." }
    """
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Use POST'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    secret = data.get('secret', '')
    expected_secret = getattr(settings, 'FORCE_PASSWORD_RESET_SECRET', '')

    if not expected_secret:
        return JsonResponse({
            'success': False,
            'error': 'FORCE_PASSWORD_RESET_SECRET is not configured on this server.'
        }, status=501)

    if secret != expected_secret:
        return JsonResponse({'success': False, 'error': 'Invalid secret key.'}, status=403)

    email = data.get('email', '').strip().lower()
    new_password = data.get('new_password', '')

    if not email or not new_password:
        return JsonResponse({'success': False, 'error': 'Email and new_password are required.'}, status=400)

    if len(new_password) < 8:
        return JsonResponse({'success': False, 'error': 'New password must be at least 8 characters.'}, status=400)

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'User not found.'}, status=404)

    user.set_password(new_password)
    user.is_verified = True
    user.is_staff = True
    user.is_superuser = True
    user.save(update_fields=['password', 'is_verified', 'is_staff', 'is_superuser'])

    return JsonResponse({
        'success': True,
        'message': f'Password reset successfully for {user.email}.'
    })


urlpatterns = [
    # Health check
    path('health/', health_check, name='health_check'),
    
    # TEMPORARY: Force password reset endpoint
    path('api/auth/force-reset-password/', force_reset_password_view, name='force-reset-password'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # API Routes
    path('api/auth/', include('apps.authentication.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/teachers/', include('apps.teachers.urls')),
    path('api/students/', include('apps.students.urls')),
    path('api/bookings/', include('apps.bookings.urls')),
    path('api/payments/', include('apps.payments.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/wishlist/', include('apps.wishlist.urls')),
    path('api/chat/', include('apps.chat.urls')),
    path('api/notifications/', include('apps.notifications.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)