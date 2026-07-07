from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel
from apps.common.utils import generate_reference_id


class Payment(TimeStampedModel):
    """
    Payment model supporting eSewa, Khalti, and Stripe.
    """

    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', _('Pending')
        PROCESSING = 'processing', _('Processing')
        COMPLETED = 'completed', _('Completed')
        FAILED = 'failed', _('Failed')
        REFUNDED = 'refunded', _('Refunded')
        CANCELLED = 'cancelled', _('Cancelled')

    class PaymentMethod(models.TextChoices):
        ESEWA = 'esewa', _('eSewa')
        KHALTI = 'khalti', _('Khalti')
        STRIPE = 'stripe', _('Stripe')

    payment_id = models.CharField(
        _('payment ID'),
        max_length=50,
        unique=True,
        default=generate_reference_id,
        editable=False,
    )
    booking = models.ForeignKey(
        'bookings.Booking',
        on_delete=models.CASCADE,
        related_name='payments',
    )
    student = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='payments_made',
    )
    teacher = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='payments_received',
    )
    amount = models.DecimalField(
        _('amount'),
        max_digits=10,
        decimal_places=2,
    )
    service_charge = models.DecimalField(
        _('service charge'),
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )
    total_amount = models.DecimalField(
        _('total amount'),
        max_digits=10,
        decimal_places=2,
    )
    payment_method = models.CharField(
        _('payment method'),
        max_length=20,
        choices=PaymentMethod.choices,
    )
    status = models.CharField(
        _('status'),
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )
    transaction_id = models.CharField(
        _('transaction ID'),
        max_length=100,
        null=True,
        blank=True,
    )
    gateway_response = models.JSONField(
        _('gateway response'),
        null=True,
        blank=True,
    )
    refund_amount = models.DecimalField(
        _('refund amount'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    refund_reason = models.TextField(
        _('refund reason'),
        max_length=500,
        null=True,
        blank=True,
    )
    refunded_at = models.DateTimeField(null=True, blank=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['payment_id']),
            models.Index(fields=['student', 'status']),
            models.Index(fields=['transaction_id']),
        ]

    def __str__(self):
        return f'{self.payment_id} - {self.amount} ({self.get_payment_method_display()})'


class Invoice(models.Model):
    """
    Invoice model for payment receipts.
    """
    payment = models.OneToOneField(
        Payment,
        on_delete=models.CASCADE,
        related_name='invoice',
    )
    invoice_number = models.CharField(
        _('invoice number'),
        max_length=50,
        unique=True,
        default=generate_reference_id,
        editable=False,
    )
    billing_address = models.TextField(_('billing address'), max_length=500, null=True, blank=True)
    notes = models.TextField(_('notes'), max_length=1000, null=True, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoices')

    def __str__(self):
        return f'Invoice {self.invoice_number}'


class Refund(models.Model):
    """
    Refund model for payment reversals.
    """
    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        related_name='refunds',
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField(max_length=500)
    is_processed = models.BooleanField(default=False)
    processed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Refund {self.amount} - {self.payment.payment_id}'