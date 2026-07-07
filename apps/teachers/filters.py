import django_filters
from django.db.models import Q
from apps.teachers.models import TeacherProfile


class TeacherFilter(django_filters.FilterSet):
    """
    Filter set for teacher search and filtering.
    """
    min_price = django_filters.NumberFilter(field_name='hourly_rate', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='hourly_rate', lookup_expr='lte')
    min_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gte')
    max_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='lte')
    min_experience = django_filters.NumberFilter(field_name='years_of_experience', lookup_expr='gte')
    max_experience = django_filters.NumberFilter(field_name='years_of_experience', lookup_expr='lte')
    teaching_mode = django_filters.ChoiceFilter(choices=TeacherProfile.TeachingMode.choices)
    experience_level = django_filters.ChoiceFilter(choices=TeacherProfile.ExperienceLevel.choices)
    is_verified = django_filters.BooleanFilter()
    is_available = django_filters.BooleanFilter()
    subject = django_filters.CharFilter(method='filter_by_subject')
    location = django_filters.CharFilter(lookup_expr='icontains')
    language = django_filters.CharFilter(method='filter_by_language')
    search = django_filters.CharFilter(method='filter_by_search')

    class Meta:
        model = TeacherProfile
        fields = [
            'min_price', 'max_price', 'min_rating', 'max_rating',
            'min_experience', 'max_experience', 'teaching_mode',
            'experience_level', 'is_verified', 'is_available',
            'subject', 'location', 'language', 'search',
        ]

    def filter_by_subject(self, queryset, name, value):
        return queryset.filter(
            Q(subjects__name__icontains=value) |
            Q(subjects__id=value)
        ).distinct()

    def filter_by_language(self, queryset, name, value):
        return queryset.filter(
            Q(languages__name__icontains=value) |
            Q(languages__code__iexact=value)
        ).distinct()

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            Q(user__first_name__icontains=value) |
            Q(user__last_name__icontains=value) |
            Q(headline__icontains=value) |
            Q(about__icontains=value) |
            Q(location__icontains=value) |
            Q(subjects__name__icontains=value)
        ).distinct()