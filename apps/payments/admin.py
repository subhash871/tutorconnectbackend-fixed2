from django.contrib import admin
from .models import Payment, Invoice, Refund


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'booking', 'student', 'teacher', 'amount', 'payment_method', 'status', 'paid_at', 'created_at']
    list_filter = ['payment_method', 'status']
    search_fields = ['payment_id', 'transaction_id', 'student__email', 'teacher__email']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'payment', 'generated_at']
    search_fields = ['invoice_number', 'payment__payment_id']


@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ['payment', 'amount', 'is_processed', 'processed_at', 'created_at']
    list_filter = ['is_processed']
    search_fields = ['payment__payment_id']
