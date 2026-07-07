from rest_framework import serializers
from apps.reviews.models import Review
from apps.bookings.models import Booking


class ReviewSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'student', 'student_name', 'teacher', 'booking',
                 'rating', 'comment', 'is_approved', 'created_at']
        read_only_fields = ['id', 'student', 'student_name', 'is_approved', 'created_at']

    def get_student_name(self, obj):
        return obj.student.get_full_name()


class ReviewCreateSerializer(serializers.ModelSerializer):
    booking = serializers.PrimaryKeyRelatedField(queryset=Booking.objects.all(), required=True)

    class Meta:
        model = Review
        fields = ['teacher', 'booking', 'rating', 'comment']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Rating must be between 1 and 5.')
        return value

    def validate(self, data):
        request = self.context['request']
        booking = data['booking']

        if booking.student_id != request.user.id:
            raise serializers.ValidationError({'booking': "This booking doesn't belong to you."})
        if booking.status != Booking.BookingStatus.COMPLETED:
            raise serializers.ValidationError({'booking': 'You can only review a completed session.'})
        if booking.teacher_profile_id != data['teacher'].id:
            raise serializers.ValidationError({'teacher': "This booking wasn't with this tutor."})

        return data

    def create(self, validated_data):
        validated_data['student'] = self.context['request'].user
        return super().create(validated_data)
