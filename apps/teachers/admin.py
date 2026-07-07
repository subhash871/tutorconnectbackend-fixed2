from django.contrib import admin
from apps.teachers.models import (
    TeacherProfile, Subject, Language, Qualification,
    Experience, Certificate, TeacherGallery, AvailabilityCalendar,
    TeacherAvailability
)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name', 'code']


class QualificationInline(admin.TabularInline):
    model = Qualification
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1


class AvailabilityCalendarInline(admin.TabularInline):
    model = AvailabilityCalendar
    extra = 7


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'hourly_rate', 'average_rating', 
                   'is_verified', 'is_available', 'teaching_mode', 'created_at']
    list_filter = ['is_verified', 'is_available', 'is_featured', 'teaching_mode', 'experience_level']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'title', 'location']
    inlines = [QualificationInline, ExperienceInline, CertificateInline, AvailabilityCalendarInline]
    filter_horizontal = ['subjects', 'languages']
    readonly_fields = ['total_students', 'total_hours', 'total_bookings', 
                      'average_rating', 'total_reviews', 'completion_rate', 'response_time']


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'degree', 'institution', 'start_year', 'end_year']
    search_fields = ['degree', 'institution', 'teacher__user__email']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'title', 'organization', 'start_date', 'end_date', 'is_current']
    search_fields = ['title', 'organization', 'teacher__user__email']


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'title', 'issuing_organization', 'issue_date']
    search_fields = ['title', 'issuing_organization']


@admin.register(TeacherGallery)
class TeacherGalleryAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'caption', 'is_primary', 'created_at']


@admin.register(AvailabilityCalendar)
class AvailabilityCalendarAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'day_of_week', 'start_time', 'end_time', 'is_available']
    list_filter = ['day_of_week', 'is_available']


@admin.register(TeacherAvailability)
class TeacherAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'date', 'start_time', 'end_time', 'is_available']
    list_filter = ['is_available']
    date_hierarchy = 'date'