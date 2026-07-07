from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


class Subject(models.Model):
    """
    Subject model for teacher subjects.
    """
    name = models.CharField(_('name'), max_length=100, unique=True)
    description = models.TextField(_('description'), max_length=500, null=True, blank=True)
    icon = models.CharField(_('icon'), max_length=50, null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Language(models.Model):
    """
    Language model for teacher languages.
    """
    name = models.CharField(_('name'), max_length=50, unique=True)
    code = models.CharField(_('code'), max_length=10, unique=True)

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')
        ordering = ['name']

    def __str__(self):
        return self.name


class TeacherProfile(TimeStampedModel):
    """
    Extended profile for teachers.
    """

    class TeachingMode(models.TextChoices):
        HOME_TUITION = 'home_tuition', _('Home Tuition')
        ONLINE_TUITION = 'online_tuition', _('Online Tuition')
        BOTH = 'both', _('Both')

    class ExperienceLevel(models.TextChoices):
        ENTRY = 'entry', _('Entry Level (0-2 years)')
        INTERMEDIATE = 'intermediate', _('Intermediate (2-5 years)')
        EXPERIENCED = 'experienced', _('Experienced (5-10 years)')
        EXPERT = 'expert', _('Expert (10+ years)')

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
        related_name='teacher_profile',
    )
    title = models.CharField(_('title'), max_length=200, null=True, blank=True)
    headline = models.CharField(_('headline'), max_length=500, null=True, blank=True)
    about = models.TextField(_('about'), max_length=5000, null=True, blank=True)
    
    # Teaching details
    teaching_mode = models.CharField(
        _('teaching mode'),
        max_length=20,
        choices=TeachingMode.choices,
        default=TeachingMode.BOTH,
    )
    experience_level = models.CharField(
        _('experience level'),
        max_length=20,
        choices=ExperienceLevel.choices,
        default=ExperienceLevel.ENTRY,
    )
    years_of_experience = models.PositiveIntegerField(
        _('years of experience'),
        default=0,
    )
    hourly_rate = models.DecimalField(
        _('hourly rate'),
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    
    # Location
    location = models.CharField(_('location'), max_length=255, null=True, blank=True)
    latitude = models.DecimalField(
        _('latitude'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        _('longitude'),
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    service_area = models.PositiveIntegerField(
        _('service area (km)'),
        default=10,
        help_text=_('Maximum distance in km the teacher is willing to travel'),
    )
    
    # Online teaching
    meeting_link = models.URLField(_('meeting link'), max_length=500, null=True, blank=True)
    
    # Media
    profile_image = models.FileField(
        _('profile image'),
        upload_to='teachers/profiles/',
        null=True,
        blank=True,
    )
    demo_video = models.FileField(
        _('demo video'),
        upload_to='teachers/demo_videos/',
        null=True,
        blank=True,
    )
    
    # Verification
    is_verified = models.BooleanField(_('verified'), default=False)
    verified_at = models.DateTimeField(null=True, blank=True)
    
    # Stats
    total_students = models.PositiveIntegerField(_('total students'), default=0)
    total_hours = models.PositiveIntegerField(_('total hours taught'), default=0)
    total_bookings = models.PositiveIntegerField(_('total bookings'), default=0)
    average_rating = models.DecimalField(
        _('average rating'),
        max_digits=3,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    total_reviews = models.PositiveIntegerField(_('total reviews'), default=0)
    completion_rate = models.DecimalField(
        _('completion rate'),
        max_digits=5,
        decimal_places=2,
        default=100.00,
        help_text=_('Percentage of completed bookings'),
    )
    response_time = models.PositiveIntegerField(
        _('response time (hours)'),
        default=24,
        help_text=_('Average response time in hours'),
    )
    
    # Social links
    website = models.URLField(_('website'), max_length=500, null=True, blank=True)
    linkedin = models.URLField(_('linkedin'), max_length=500, null=True, blank=True)
    youtube = models.URLField(_('youtube'), max_length=500, null=True, blank=True)
    
    # Settings
    is_available = models.BooleanField(_('available for booking'), default=True)
    is_featured = models.BooleanField(_('featured'), default=False)
    max_students = models.PositiveIntegerField(_('max students'), default=10)
    
    # Many-to-many relationships
    subjects = models.ManyToManyField(
        Subject,
        related_name='teachers',
        blank=True,
    )
    languages = models.ManyToManyField(
        Language,
        related_name='teachers',
        blank=True,
    )

    class Meta:
        verbose_name = _('teacher profile')
        verbose_name_plural = _('teacher profiles')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'is_verified']),
            models.Index(fields=['hourly_rate']),
            models.Index(fields=['average_rating']),
            models.Index(fields=['years_of_experience']),
            models.Index(fields=['teaching_mode']),
            models.Index(fields=['is_available']),
            models.Index(fields=['location']),
        ]

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.title or "Teacher"}'

    def update_rating(self):
        """Update average rating from reviews."""
        from apps.reviews.models import Review
        reviews = Review.objects.filter(teacher=self)
        if reviews.exists():
            self.average_rating = reviews.aggregate(
                avg=models.Avg('rating')
            )['avg']
            self.total_reviews = reviews.count()
            self.save(update_fields=['average_rating', 'total_reviews'])


class Qualification(models.Model):
    """
    Teacher qualifications/education.
    """
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='qualifications',
    )
    degree = models.CharField(_('degree'), max_length=200)
    institution = models.CharField(_('institution'), max_length=300)
    field_of_study = models.CharField(_('field of study'), max_length=200)
    start_year = models.PositiveIntegerField(_('start year'))
    end_year = models.PositiveIntegerField(_('end year'), null=True, blank=True)
    is_current = models.BooleanField(_('currently studying'), default=False)
    description = models.TextField(_('description'), max_length=1000, null=True, blank=True)
    certificate = models.FileField(
        _('certificate'),
        upload_to='teachers/qualifications/',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('qualification')
        verbose_name_plural = _('qualifications')
        ordering = ['-end_year', '-start_year']

    def __str__(self):
        return f'{self.degree} - {self.institution}'


class Experience(models.Model):
    """
    Teacher work experience.
    """
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='experiences',
    )
    title = models.CharField(_('title'), max_length=200)
    organization = models.CharField(_('organization'), max_length=300)
    location = models.CharField(_('location'), max_length=200, null=True, blank=True)
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'), null=True, blank=True)
    is_current = models.BooleanField(_('current position'), default=False)
    description = models.TextField(_('description'), max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('experience')
        verbose_name_plural = _('experiences')
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f'{self.title} at {self.organization}'


class Certificate(models.Model):
    """
    Teacher certificates and achievements.
    """
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='certificates',
    )
    title = models.CharField(_('title'), max_length=200)
    issuing_organization = models.CharField(_('issuing organization'), max_length=300)
    credential_id = models.CharField(_('credential ID'), max_length=100, null=True, blank=True)
    credential_url = models.URLField(_('credential URL'), max_length=500, null=True, blank=True)
    issue_date = models.DateField(_('issue date'))
    expiry_date = models.DateField(_('expiry date'), null=True, blank=True)
    does_not_expire = models.BooleanField(_('does not expire'), default=False)
    file = models.FileField(
        _('certificate file'),
        upload_to='teachers/certificates/',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('certificate')
        verbose_name_plural = _('certificates')
        ordering = ['-issue_date']

    def __str__(self):
        return self.title


class TeacherGallery(models.Model):
    """
    Teacher gallery images.
    """
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='gallery_images',
    )
    image = models.FileField(upload_to='teachers/gallery/')
    caption = models.CharField(_('caption'), max_length=200, null=True, blank=True)
    is_primary = models.BooleanField(_('primary image'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('gallery image')
        verbose_name_plural = _('gallery images')
        ordering = ['-is_primary', '-created_at']

    def __str__(self):
        return f'Gallery image for {self.teacher}'


class AvailabilityCalendar(models.Model):
    """
    Teacher availability calendar.
    """
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 0, _('Monday')
        TUESDAY = 1, _('Tuesday')
        WEDNESDAY = 2, _('Wednesday')
        THURSDAY = 3, _('Thursday')
        FRIDAY = 4, _('Friday')
        SATURDAY = 5, _('Saturday')
        SUNDAY = 6, _('Sunday')

    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='availability',
    )
    day_of_week = models.IntegerField(
        _('day of week'),
        choices=DayOfWeek.choices,
    )
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    is_available = models.BooleanField(_('available'), default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('availability')
        verbose_name_plural = _('availabilities')
        unique_together = ['teacher', 'day_of_week', 'start_time']
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f'{self.teacher} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}'


class TeacherAvailability(models.Model):
    """
    Specific date availability (for exceptions or specific dates).
    """
    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.CASCADE,
        related_name='specific_availability',
    )
    date = models.DateField(_('date'))
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))
    is_available = models.BooleanField(_('available'), default=True)
    reason = models.CharField(_('reason'), max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('specific availability')
        verbose_name_plural = _('specific availabilities')
        unique_together = ['teacher', 'date', 'start_time']
        ordering = ['date', 'start_time']

    def __str__(self):
        status = 'Available' if self.is_available else 'Unavailable'
        return f'{self.teacher} - {self.date} {self.start_time}-{self.end_time} ({status})'