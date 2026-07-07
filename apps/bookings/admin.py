from django.contrib import admin
from .models import Booking, RescheduleRequest


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_id', 'student', 'teacher', 'teacher_profile', 'status', 'preferred_date', 'hourly_rate', 'is_paid', 'created_at']
    list_filter = ['status', 'teaching_mode', 'is_paid']
    search_fields = ['booking_id', 'student__email', 'teacher__email', 'teacher_profile__user__email']
    date_hierarchy = 'preferred_date'


@admin.register(RescheduleRequest)
class RescheduleRequestAdmin(admin.ModelAdmin):
    list_display = ['booking', 'requested_by', 'new_date', 'is_approved', 'created_at']
    list_filter = ['is_approved']
    search_fields = ['booking__booking_id', 'requested_by__email']
