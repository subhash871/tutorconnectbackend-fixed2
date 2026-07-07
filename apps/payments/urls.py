from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payments.views import PaymentViewSet, InvoiceViewSet, esewa_webhook, khalti_webhook, stripe_webhook

app_name = 'payments'

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')
router.register(r'invoices', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls)),
    path('webhook/esewa/', esewa_webhook, name='esewa-webhook'),
    path('webhook/khalti/', khalti_webhook, name='khalti-webhook'),
    path('webhook/stripe/', stripe_webhook, name='stripe-webhook'),
]