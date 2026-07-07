from rest_framework import serializers
from apps.payments.models import Payment, Invoice, Refund


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['payment_id', 'status', 'gateway_response', 'paid_at']


class PaymentCreateSerializer(serializers.Serializer):
    booking_id = serializers.CharField(required=True)
    payment_method = serializers.ChoiceField(choices=['esewa', 'khalti', 'stripe'])


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class RefundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refund
        fields = ['id', 'amount', 'reason', 'is_processed', 'created_at']
        read_only_fields = ['id', 'is_processed', 'created_at']