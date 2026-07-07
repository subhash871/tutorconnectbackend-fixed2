from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.bookings.views import BookingViewSet, RescheduleRequestViewSet

app_name = 'bookings'

router = DefaultRouter()
router.register(r'', BookingViewSet, basename='booking')
router.register(r'reschedule-requests', RescheduleRequestViewSet, basename='reschedule-request')

urlpatterns = [
    path('', include(router.urls)),
]