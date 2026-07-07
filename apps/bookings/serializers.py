from rest_framework import serializers
from apps.bookings.models import Booking, RescheduleRequest
from apps.teachers.serializers import SubjectSerializer


class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'teacher', 'subject', 'teaching_mode', 'preferred_date',
            'start_time', 'end_time', 'duration_hours', 'location',
            'latitude', 'longitude', 'student_notes',
        ]

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError('End time must be after start time.')

        # Prevent double-booking: reject if the same teacher already has an
        # active booking that overlaps this date/time window.
        conflicts = Booking.objects.filter(
            teacher=data['teacher'],
            preferred_date=data['preferred_date'],
            status__in=[Booking.BookingStatus.PENDING, Booking.BookingStatus.ACCEPTED],
            start_time__lt=data['end_time'],
            end_time__gt=data['start_time'],
        )
        if self.instance is not None:
            conflicts = conflicts.exclude(pk=self.instance.pk)
        if conflicts.exists():
            raise serializers.ValidationError(
                'This tutor already has a booking that overlaps this time slot. '
                'Please choose a different time.'
            )

        return data


class BookingListSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = [
            'id', 'booking_id', 'student_name', 'teacher_name',
            'subject_name', 'status', 'teaching_mode', 'preferred_date',
            'start_time', 'end_time', 'total_amount', 'is_paid',
            'created_at',
        ]

    def get_student_name(self, obj):
        return obj.student.get_full_name()

    def get_teacher_name(self, obj):
        return obj.teacher.get_full_name()

    def get_subject_name(self, obj):
        return obj.subject.name if obj.subject else None


class BookingDetailSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    subject_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'

    def get_student_name(self, obj):
        return obj.student.get_full_name()

    def get_teacher_name(self, obj):
        return obj.teacher.get_full_name()

    def get_subject_name(self, obj):
        return obj.subject.name if obj.subject else None


class RescheduleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RescheduleRequest
        fields = ['id', 'booking', 'new_date', 'new_start_time', 'new_end_time', 'reason']
        read_only_fields = ['id']