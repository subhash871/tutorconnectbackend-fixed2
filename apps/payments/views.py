import logging

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
from apps.payments.models import Payment, Invoice, Refund
from apps.payments.serializers import (
    PaymentSerializer, PaymentCreateSerializer, InvoiceSerializer, RefundSerializer
)
from apps.payments.gateways import verify_payment_with_gateway, GatewayVerificationError
from apps.bookings.models import Booking
from apps.notifications.tasks import create_notification

logger = logging.getLogger(__name__)


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Payment.objects.all()
        return Payment.objects.filter(student=user) | Payment.objects.filter(teacher=user)

    @action(detail=False, methods=['post'])
    def initiate_payment(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        booking = Booking.objects.get(booking_id=serializer.validated_data['booking_id'])

        if booking.student_id != request.user.id:
            return Response({'error': "This booking doesn't belong to you."}, status=status.HTTP_403_FORBIDDEN)
        if booking.is_paid:
            return Response({'error': 'This booking has already been paid for.'}, status=status.HTTP_400_BAD_REQUEST)

        payment, _created = Payment.objects.get_or_create(
            booking=booking,
            status='pending',
            defaults={
                'student': booking.student,
                'teacher': booking.teacher,
                'amount': booking.total_amount,
                'total_amount': booking.total_amount,
                'payment_method': serializer.validated_data['payment_method'],
            },
        )

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def verify_payment(self, request, pk=None):
        payment = self.get_object()

        if payment.student_id != request.user.id and request.user.role != 'admin':
            return Response({'error': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)

        if payment.status == 'completed':
            return Response({'message': 'Payment already verified.'})

        transaction_id = request.data.get('transaction_id')
        gateway_data = request.data.get('gateway_data', {})

        if not transaction_id:
            return Response({'error': 'transaction_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = verify_payment_with_gateway(payment, transaction_id, gateway_data)
        except GatewayVerificationError as exc:
            return Response({'error': str(exc)}, status=status.HTTP_502_BAD_GATEWAY)

        payment.transaction_id = transaction_id
        payment.gateway_response = result['raw']

        if not result['verified']:
            payment.status = 'failed'
            payment.save()
            return Response(
                {'error': f"Gateway did not confirm this payment ({result.get('reason') or 'not completed'})."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        payment.status = 'completed'
        payment.paid_at = timezone.now()
        payment.save()

        booking = payment.booking
        booking.is_paid = True
        booking.save(update_fields=['is_paid'])

        create_notification.delay(
            payment.teacher_id, 'payment_received', 'Payment received',
            f'{payment.student.get_full_name()} paid Rs. {payment.amount} for a booking.',
            {'payment_id': payment.id, 'booking_id': booking.id},
        )

        return Response({'message': 'Payment verified successfully.'})

    @action(detail=True, methods=['post'])
    def refund(self, request, pk=None):
        payment = self.get_object()

        if request.user.role != 'admin' and payment.student_id != request.user.id:
            return Response({'error': 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        if payment.status != 'completed':
            return Response({'error': 'Only completed payments can be refunded.'}, status=status.HTTP_400_BAD_REQUEST)

        amount = request.data.get('amount', payment.amount)
        reason = request.data.get('reason', '')

        refund = Refund.objects.create(
            payment=payment,
            amount=amount,
            reason=reason,
        )

        payment.status = 'refunded'
        payment.refund_amount = amount
        payment.refund_reason = reason
        payment.refunded_at = timezone.now()
        payment.save()

        return Response({'message': 'Refund processed.', 'refund_id': refund.id})

    @action(detail=False, methods=['get'])
    def my_transactions(self, request):
        payments = self.get_queryset()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(payment__student=self.request.user)


def _mark_payment_completed(payment, transaction_id, raw_data):
    if payment.status == 'completed':
        return
    payment.transaction_id = transaction_id
    payment.gateway_response = raw_data
    payment.status = 'completed'
    payment.paid_at = timezone.now()
    payment.save()
    payment.booking.is_paid = True
    payment.booking.save(update_fields=['is_paid'])
    create_notification.delay(
        payment.teacher_id, 'payment_received', 'Payment received',
        f'{payment.student.get_full_name()} paid Rs. {payment.amount} for a booking.',
        {'payment_id': payment.id, 'booking_id': payment.booking_id},
    )


@api_view(['POST'])
@permission_classes([AllowAny])
def esewa_webhook(request):
    """eSewa payment webhook — verifies with eSewa's status API before trusting it."""
    data = request.data
    transaction_uuid = data.get('transaction_uuid')
    payment_id = data.get('payment_id') or data.get('transaction_uuid')

    payment = Payment.objects.filter(transaction_id=transaction_uuid).first() or \
        Payment.objects.filter(payment_id=payment_id).first()
    if not payment:
        logger.warning('eSewa webhook: no matching payment for %s', data)
        return Response({'status': 'ignored', 'reason': 'unknown payment'}, status=status.HTTP_404_NOT_FOUND)

    try:
        result = verify_payment_with_gateway(payment, transaction_uuid, data)
    except GatewayVerificationError as exc:
        logger.error('eSewa webhook verification failed: %s', exc)
        return Response({'status': 'error'}, status=status.HTTP_502_BAD_GATEWAY)

    if result['verified']:
        _mark_payment_completed(payment, transaction_uuid, result['raw'])
    return Response({'status': 'received'})


@api_view(['POST'])
@permission_classes([AllowAny])
def khalti_webhook(request):
    """Khalti payment webhook — verifies with Khalti's lookup API before trusting it."""
    data = request.data
    pidx = data.get('pidx')

    payment = Payment.objects.filter(transaction_id=pidx).first()
    if not payment:
        logger.warning('Khalti webhook: no matching payment for pidx=%s', pidx)
        return Response({'status': 'ignored', 'reason': 'unknown payment'}, status=status.HTTP_404_NOT_FOUND)

    try:
        result = verify_payment_with_gateway(payment, pidx, data)
    except GatewayVerificationError as exc:
        logger.error('Khalti webhook verification failed: %s', exc)
        return Response({'status': 'error'}, status=status.HTTP_502_BAD_GATEWAY)

    if result['verified']:
        _mark_payment_completed(payment, pidx, result['raw'])
    return Response({'status': 'received'})


@api_view(['POST'])
@permission_classes([AllowAny])
def stripe_webhook(request):
    """Stripe webhook — verifies the signature before trusting the payload at all."""
    if not settings.STRIPE_WEBHOOK_SECRET:
        logger.error('Stripe webhook called but STRIPE_WEBHOOK_SECRET is not configured.')
        return Response({'status': 'error', 'reason': 'not configured'}, status=status.HTTP_501_NOT_IMPLEMENTED)

    import stripe

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except (ValueError, stripe.error.SignatureVerificationError):
        logger.warning('Stripe webhook signature verification failed.')
        return Response({'status': 'invalid signature'}, status=status.HTTP_400_BAD_REQUEST)

    if event['type'] == 'payment_intent.succeeded':
        intent = event['data']['object']
        payment = Payment.objects.filter(transaction_id=intent['id']).first()
        if payment:
            _mark_payment_completed(payment, intent['id'], intent)
        else:
            logger.warning('Stripe webhook: no matching payment for PaymentIntent %s', intent['id'])

    return Response({'status': 'received'})
