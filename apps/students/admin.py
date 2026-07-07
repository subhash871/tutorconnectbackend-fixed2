from django.contrib import admin
from .models import StudentProfile, StudentPreference


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'grade_level', 'school', 'total_bookings', 'total_hours_learned', 'created_at']
    search_fields = ['user__email', 'user__username', 'school', 'parent_name']
    list_filter = ['grade_level']


@admin.register(StudentPreference)
class StudentPreferenceAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'preferred_gender', 'preferred_experience', 'created_at']
    search_fields = ['student__user__email', 'subject__name']
    list_filter = ['preferred_gender']
