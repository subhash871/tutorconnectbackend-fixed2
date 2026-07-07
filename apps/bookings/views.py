from django.db import models
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from apps.bookings.models import Booking, RescheduleRequest
from apps.bookings.serializers import (
    BookingCreateSerializer, BookingListSerializer,
    BookingDetailSerializer, RescheduleRequestSerializer
)
from apps.common.permissions import IsStudent, IsTeacher
from apps.notifications.tasks import create_notification
from apps.chat.models import Conversation 

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing bookings.
    """
    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        elif self.action == 'list':
            return BookingListSerializer
        return BookingDetailSerializer

    def get_permissions(self):
        if self.action in ['create', 'cancel', 'reschedule_request']:
            return [permissions.IsAuthenticated(), IsStudent()]
        elif self.action in ['accept', 'reject', 'complete']:
            return [permissions.IsAuthenticated(), IsTeacher()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'teacher':
            return Booking.objects.filter(teacher=user).select_related(
                'student', 'teacher', 'subject', 'teacher_profile'
            )
        elif user.role == 'student':
            return Booking.objects.filter(student=user).select_related(
                'student', 'teacher', 'subject', 'teacher_profile'
            )
        return Booking.objects.filter(
            models.Q(student=user) | models.Q(teacher=user)
        ).select_related('student', 'teacher', 'subject', 'teacher_profile')

    def perform_create(self, serializer):
        teacher = serializer.validated_data['teacher']
        teacher_profile = teacher.teacher_profile
        hourly_rate = teacher_profile.hourly_rate
        duration = serializer.validated_data['duration_hours']
        total_amount = float(hourly_rate) * float(duration)

        booking = serializer.save(
            student=self.request.user,
            teacher_profile=teacher_profile,
            hourly_rate=hourly_rate,
            total_amount=total_amount,
        )
        create_notification.delay(
            booking.teacher_id, 'booking_request', 'New booking request',
            f'{self.request.user.get_full_name()} requested a session on {booking.preferred_date}.',
            {'booking_id': booking.id},
        )

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'pending':
            return Response({'error': 'Booking cannot be accepted.'}, status=400)
        booking.status = 'accepted'
        booking.accepted_at = timezone.now()
        booking.save()

        conversation, created = Conversation.objects.get_or_create(booking=booking)
        if created:
            conversation.participants.add(booking.student, booking.teacher)
        create_notification.delay(
            booking.student_id, 'booking_accepted', 'Booking accepted',
            f'{booking.teacher.get_full_name()} accepted your booking request.',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Booking accepted.'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'pending':
            return Response({'error': 'Booking cannot be rejected.'}, status=400)
        booking.status = 'rejected'
        booking.rejected_at = timezone.now()
        booking.save()
        create_notification.delay(
            booking.student_id, 'booking_rejected', 'Booking declined',
            f'{booking.teacher.get_full_name()} declined your booking request.',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Booking rejected.'})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.status in ['completed', 'cancelled']:
            return Response({'error': 'Booking cannot be cancelled.'}, status=400)
        reason = request.data.get('reason', '')
        booking.status = 'cancelled'
        booking.cancelled_at = timezone.now()
        booking.cancellation_reason = reason
        booking.save()
        create_notification.delay(
            booking.teacher_id, 'booking_cancelled', 'Booking cancelled',
            f'{booking.student.get_full_name()} cancelled their booking.',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Booking cancelled.'})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'accepted':
            return Response({'error': 'Booking cannot be completed.'}, status=400)
        booking.status = 'completed'
        booking.completed_at = timezone.now()
        booking.save()
        create_notification.delay(
            booking.student_id, 'booking_completed', 'Session completed',
            f'Your session with {booking.teacher.get_full_name()} is marked complete. Leave a review!',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Booking completed.'})

    @action(detail=True, methods=['post'])
    def reschedule_request(self, request, pk=None):
        booking = self.get_object()
        serializer = RescheduleRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(booking=booking, requested_by=request.user)
        create_notification.delay(
            booking.teacher_id, 'booking_rescheduled', 'Reschedule requested',
            f'{request.user.get_full_name()} requested to reschedule a booking.',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Reschedule request submitted.'})


class RescheduleRequestViewSet(viewsets.ModelViewSet):
    serializer_class = RescheduleRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RescheduleRequest.objects.filter(
            booking__teacher=self.request.user
        ) | RescheduleRequest.objects.filter(
            booking__student=self.request.user
        )

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        reschedule = self.get_object()
        booking = reschedule.booking
        booking.status = 'rescheduled'
        booking.preferred_date = reschedule.new_date
        booking.start_time = reschedule.new_start_time
        booking.end_time = reschedule.new_end_time
        booking.rescheduled_at = timezone.now()
        booking.reschedule_count += 1
        booking.save()
        reschedule.is_approved = True
        reschedule.save()
        create_notification.delay(
            booking.student_id, 'booking_rescheduled', 'Reschedule approved',
            f'Your booking was rescheduled to {booking.preferred_date}.',
            {'booking_id': booking.id},
        )
        return Response({'message': 'Reschedule approved.'})