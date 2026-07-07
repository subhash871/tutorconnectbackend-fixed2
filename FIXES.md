# Fixes applied to tutor-connect-backend

This document lists every change made on top of the original repo, grouped by
severity. Each item was verified against a live-running instance of this
backend (and/or the automated test suite) before being included here.

## 🔴 Security-critical

**1. Payments were never actually verified — `apps/payments/views.py`, new `apps/payments/gateways.py`**
`verify_payment` used to trust whatever `status` the client sent, with no
gateway call at all. It now calls real verification APIs:
- eSewa: `GET /api/epay/transaction/status/` status-check endpoint
- Khalti: `POST /api/v2/epayment/lookup/` lookup endpoint
- Stripe: `PaymentIntent.retrieve()` + webhook signature verification via
  `stripe.Webhook.construct_event`

If a gateway's credentials aren't configured in `.env`, verification falls
back to a manual-confirm path **that only works when `DEBUG=True`** — so a
misconfigured production deployment can never silently "verify" a payment
that was never actually paid. The three webhook endpoints
(`esewa_webhook`, `khalti_webhook`, `stripe_webhook`) now actually verify and
update the payment record instead of being empty stubs.

**2. Anyone could edit or delete anyone else's review — `apps/reviews/views.py`**
`get_permissions()` allowed any authenticated user to `PATCH`/`DELETE` any
review by ID, and `get_queryset()` didn't scope those actions to the
requester. Fixed with an object-level `IsReviewOwnerOrReadOnly` permission
plus a scoped queryset (non-owners now get a 404, not a 403, so review
ownership isn't leaked).

**3. Reviews could be created without a real completed booking — `apps/reviews/serializers.py`**
`booking` is now a required field on review creation, and creation is
rejected unless: the booking belongs to the requesting student, the booking
status is `completed`, and the booking's teacher matches the review's
teacher. (The field was previously optional, which also meant the
booking-ownership/completion check silently never ran if it was omitted.)

**4. Reviews required silent manual admin approval — `apps/reviews/models.py`**
`is_approved` defaulted to `False` with no bulk-approval tool in the admin,
so every new review was invisible until someone found and checked a box in
Django admin. Now defaults to `True` (visible immediately); the field is
still there for future moderation.

## 🟠 Missing functionality, now implemented

**5. No double-booking prevention — `apps/bookings/serializers.py`**
`BookingCreateSerializer.validate()` now rejects a new booking if the same
teacher already has a `pending`/`accepted` booking with an overlapping
date/time window.

**6. Chat websockets were referenced but didn't exist — `apps/chat/consumers.py`, `apps/chat/routing.py`, `config/asgi.py`**
`config/asgi.py` referenced `apps.chat.routing.websocket_urlpatterns`
without ever importing `apps.chat` — this would crash immediately under a
real ASGI server. Added a working `ChatConsumer` (message send, typing
indicator, read receipts, all scoped to conversation participants) and its
routing, and fixed `asgi.py`'s import order so Django's app registry is
populated before anything touches models. Connect at
`ws://<host>/ws/chat/<conversation_id>/`. (The React frontend still uses
REST polling; wiring the frontend to this is a good next step but wasn't
required for the backend to be internally consistent.)

**7. Google OAuth login was a placeholder — `apps/authentication/views.py`**
Now verifies the ID token with `google-auth` against `GOOGLE_OAUTH_CLIENT_ID`,
finds-or-creates the user (auto-verified, unusable local password), and
issues JWTs the same way normal login does. Returns `501` with a clear
message if `GOOGLE_OAUTH_CLIENT_ID` isn't configured, rather than silently
"succeeding" with no user.

**8. In-app notifications were never triggered by anything — `apps/bookings/views.py`, `apps/payments/views.py`, `apps/reviews/views.py`, `apps/chat/views.py`, `apps/users/views.py`**
The `create_notification` Celery task existed and worked, but nothing in the
app ever called it — the notification feed would always be empty regardless
of activity. Wired it into: booking created/accepted/rejected/cancelled/
completed/reschedule-requested/reschedule-approved, payment received,
new review, new chat message, and teacher-approved.

**9. `apps/chat/views.py` `mark_read` used a broken `__import__()` call**
`__import__('django.utils.timezone').now()` actually returns the top-level
`django` package (not the `timezone` submodule), so this raised
`AttributeError` on every call — meaning opening a chat thread and marking
it read would 500 every time. Replaced with a normal `from django.utils
import timezone` import.

**10. Teacher profiles weren't auto-created on registration — `apps/users/signals.py`**
The post-save signal created a `StudentProfile` for new students but had no
equivalent for teachers. New teacher accounts now get a starter
`TeacherProfile` (unavailable, `hourly_rate=0`) immediately, matching the
student-side behavior; the teacher dashboard's "create/edit profile" flow
now always resolves to an update instead of needing a separate create step.

## 🟡 Environment / configuration fixes

**11. `UserViewSet.get_permissions()` blocked every non-admin from `/api/users/me/`**
(Already fixed in the previous round — included here for completeness.)
`me`, `login_history`, and `deactivate` now correctly require only
`IsAuthenticated` instead of falling through to `IsAdmin`.

**12. `config/__init__.py` was missing the Celery-Django hookup**
(Already fixed previously.) Without `from .celery import app as celery_app`,
`@shared_task`-decorated functions bind to an unconfigured default Celery
app, causing background email/notification tasks to attempt a connection to
the wrong broker.

**13. `requirements.txt` was missing packages actually required by `settings.py`**
Added `drf-spectacular-sidecar`, `whitenoise`, `requests` (already a
transitive dependency, now explicit), and `google-auth` (needed for fix #7).

**14. Wrong Django app label for Cloudinary — `config/settings.py`**
`INSTALLED_APPS.append('django_cloudinary_storage')` referenced an app that
doesn't exist; the package actually registers as `cloudinary_storage`.

**15. `.env.example` shipped fake-but-truthy placeholder values**
Values like `STRIPE_SECRET_KEY=your-stripe-secret-key` are non-empty, so a
plain `cp .env.example .env` used to silently enable code paths that expect
real credentials. All credential-like fields now default to blank (with a
comment explaining what happens when they're left blank vs filled in), so a
fresh setup safely uses dev-mode fallbacks until real keys are added.

**16. Django 5.0.1 crashes on Python 3.14 — `apps/common/py314_compat.py`, `apps/common/apps.py`**
`django.template.context.BaseContext.__copy__` uses a `copy(super())` trick
to shallow-copy template contexts. Python 3.14 changed `super` proxy
internals enough that this now raises
`AttributeError: 'super' object has no attribute 'dicts' and no __dict__
for setting new attributes` — this surfaces anywhere Django copies a
template context, most visibly in the admin's changelist pages (e.g.
`/admin/students/studentprofile/`, `/admin/teachers/teacherprofile/`).
This is a genuine Django/Python version incompatibility, not something in
this codebase, but Django 5.0.1 predates Python 3.14 by a wide margin and
won't be patched for it. Rather than editing Django's installed source
(which would be silently undone on every `pip install`), added a startup
monkeypatch in `CommonConfig.ready()` that replaces `__copy__` with a
version-independent equivalent. It's guarded to only activate on Python
3.14+, so it's a complete no-op on any Python version Django already
supports natively — verified via the automated test suite plus a targeted
test that forces the patch to apply and confirms it produces identical
output to Django's original implementation.

If this project later upgrades to a Django version with native Python 3.14
support (5.2+ / 6.0+ fixed this upstream), this patch can be deleted along
with its `ready()` hook.

## Known remaining gaps (not fixed in this pass)

- **No automated tests per app** — only the one end-to-end
  `tests/test_happy_path.py` (which was updated to match the new, stricter
  payment/review behavior, and still passes).
- **Invoices are DB records only** — no PDF generation/download.
- **Push notifications (FCM) have no send path** — `PushDevice` registration
  works, but nothing calls Firebase to actually deliver a push. In-app
  notifications (fix #8) are unaffected by this.
- **The React frontend still uses polling for chat**, not the new
  websocket endpoint from fix #6.
