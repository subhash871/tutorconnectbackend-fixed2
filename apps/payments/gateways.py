"""
Real gateway verification helpers for eSewa, Khalti, and Stripe.

Each function returns a dict: {"verified": bool, "raw": <gateway response>, "reason": str|None}

If a gateway's credentials aren't configured in settings, verification falls
back to a clearly-labeled manual/dev mode that ONLY works when DEBUG=True,
so a misconfigured production deployment can never silently "verify" a
payment that was never actually paid.
"""
import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


class GatewayVerificationError(Exception):
    pass


def _dev_fallback_only(payment, transaction_id, gateway_data):
    if not settings.DEBUG:
        raise GatewayVerificationError(
            'Payment gateway credentials are not configured on the server. '
            'Contact support instead of retrying.'
        )
    logger.warning(
        'DEV-MODE payment verification used for payment %s (no gateway '
        'credentials configured). This path is disabled when DEBUG=False.',
        payment.id,
    )
    return {
        'verified': bool(gateway_data.get('status') == 'success'),
        'raw': {'dev_mode': True, **gateway_data},
        'reason': None,
    }


def verify_esewa(payment, transaction_id, gateway_data):
    """
    Verify a transaction against eSewa's status-check API.
    Docs: https://developer.esewa.com.np/pages/status-check
    """
    if not settings.ESEWA_MERCHANT_CODE:
        return _dev_fallback_only(payment, transaction_id, gateway_data)

    try:
        resp = requests.get(
            'https://epay.esewa.com.np/api/epay/transaction/status/',
            params={
                'product_code': settings.ESEWA_MERCHANT_CODE,
                'total_amount': str(payment.total_amount),
                'transaction_uuid': transaction_id,
            },
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        logger.exception('eSewa verification request failed for payment %s', payment.id)
        raise GatewayVerificationError('Could not reach eSewa to verify this payment.') from exc

    verified = data.get('status') == 'COMPLETE'
    return {'verified': verified, 'raw': data, 'reason': None if verified else data.get('status')}


def verify_khalti(payment, transaction_id, gateway_data):
    """
    Verify a transaction against Khalti's ePayment lookup API.
    Docs: https://docs.khalti.com/khalti-epayment/#lookup-api
    """
    if not settings.KHALTI_SECRET_KEY:
        return _dev_fallback_only(payment, transaction_id, gateway_data)

    try:
        resp = requests.post(
            'https://khalti.com/api/v2/epayment/lookup/',
            headers={'Authorization': f'Key {settings.KHALTI_SECRET_KEY}'},
            json={'pidx': transaction_id},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as exc:
        logger.exception('Khalti verification request failed for payment %s', payment.id)
        raise GatewayVerificationError('Could not reach Khalti to verify this payment.') from exc

    verified = data.get('status') == 'Completed'
    return {'verified': verified, 'raw': data, 'reason': None if verified else data.get('status')}


def verify_stripe(payment, transaction_id, gateway_data):
    """
    Verify a PaymentIntent directly with Stripe's API.
    `transaction_id` is expected to be a Stripe PaymentIntent id (pi_...).
    """
    if not settings.STRIPE_SECRET_KEY:
        return _dev_fallback_only(payment, transaction_id, gateway_data)

    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        intent = stripe.PaymentIntent.retrieve(transaction_id)
    except stripe.error.StripeError as exc:
        logger.exception('Stripe verification failed for payment %s', payment.id)
        raise GatewayVerificationError('Could not verify this payment with Stripe.') from exc

    verified = intent.status == 'succeeded'
    return {'verified': verified, 'raw': dict(intent), 'reason': None if verified else intent.status}


VERIFIERS = {
    'esewa': verify_esewa,
    'khalti': verify_khalti,
    'stripe': verify_stripe,
}


def verify_payment_with_gateway(payment, transaction_id, gateway_data):
    """
    Dispatch to the correct gateway's verifier based on payment.payment_method.
    Raises GatewayVerificationError on a hard failure (network/config issue).
    Returns the verifier's result dict otherwise (caller checks ["verified"]).
    """
    verifier = VERIFIERS.get(payment.payment_method)
    if verifier is None:
        raise GatewayVerificationError(f'Unsupported payment method: {payment.payment_method}')
    return verifier(payment, transaction_id, gateway_data or {})
