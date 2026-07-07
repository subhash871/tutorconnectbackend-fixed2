# TutorConnect Nepal Thunder Client API Guide

Base URL:

```txt
http://127.0.0.1:8000
```

Important: all Django API URLs in this project use a trailing slash `/`. For POST requests, missing the trailing slash can return a Django RuntimeError.

Default JSON headers:

```txt
Content-Type: application/json
Accept: application/json
```

For protected endpoints, add:

```txt
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 1. Register Student

```http
POST http://127.0.0.1:8000/api/auth/register/
```

Body:

```json
{
  "email": "student1@test.com",
  "username": "student1",
  "password": "Password123",
  "password2": "Password123",
  "first_name": "Student",
  "last_name": "One",
  "phone_number": "9812345678",
  "role": "student"
}
```

Expected success:

```json
{
  "success": true,
  "message": "Registration successful. Please verify your email.",
  "data": {
    "user": {},
    "tokens": {
      "refresh": "...",
      "access": "..."
    }
  }
}
```

## 2. Register Teacher

```http
POST http://127.0.0.1:8000/api/auth/register/
```

Body:

```json
{
  "email": "teacher1@test.com",
  "username": "teacher1",
  "password": "Password123",
  "password2": "Password123",
  "first_name": "Teacher",
  "last_name": "One",
  "phone_number": "9823456789",
  "role": "teacher"
}
```

Teacher accounts may need `is_verified=true` and `is_teacher_approved=true` from Django Admin before they appear in public teacher listings.

## 3. Login

```http
POST http://127.0.0.1:8000/api/auth/login/
```

Body:

```json
{
  "email": "student1@test.com",
  "password": "Password123"
}
```

Copy `data.tokens.access` and use it as the Bearer token for protected requests.

## 4. Refresh Token

```http
POST http://127.0.0.1:8000/api/auth/refresh/
```

Body:

```json
{
  "refresh": "YOUR_REFRESH_TOKEN"
}
```

## 5. Logout

Requires Bearer token.

```http
POST http://127.0.0.1:8000/api/auth/logout/
```

Body:

```json
{
  "refresh": "YOUR_REFRESH_TOKEN"
}
```

## 6. Auth Utility Endpoints

```http
POST http://127.0.0.1:8000/api/auth/verify-email/
POST http://127.0.0.1:8000/api/auth/verify-otp/
POST http://127.0.0.1:8000/api/auth/resend-otp/
POST http://127.0.0.1:8000/api/auth/forgot-password/
POST http://127.0.0.1:8000/api/auth/reset-password/
POST http://127.0.0.1:8000/api/auth/change-password/
POST http://127.0.0.1:8000/api/auth/google/
```

Verify email body:

```json
{
  "email": "student1@test.com",
  "otp": "123456"
}
```

Resend OTP body:

```json
{
  "email": "student1@test.com",
  "purpose": "email_verification"
}
```

Change password body:

```json
{
  "old_password": "Password123",
  "new_password": "NewPassword123",
  "new_password2": "NewPassword123"
}
```

## 7. Current User

Requires Bearer token.

```http
GET http://127.0.0.1:8000/api/users/me/
```

Update current user:

```http
PATCH http://127.0.0.1:8000/api/users/me/
```

Body:

```json
{
  "first_name": "Updated",
  "last_name": "Student",
  "phone_number": "9812345670",
  "city": "Kathmandu",
  "address": "Baneshwor"
}
```

Other user endpoints:

```http
GET  http://127.0.0.1:8000/api/users/
GET  http://127.0.0.1:8000/api/users/{id}/
GET  http://127.0.0.1:8000/api/users/login_history/
POST http://127.0.0.1:8000/api/users/deactivate/
POST http://127.0.0.1:8000/api/users/{id}/approve_teacher/
```

## 8. Subjects

Public GET:

```http
GET http://127.0.0.1:8000/api/teachers/subjects/
```

Create subject:

```http
POST http://127.0.0.1:8000/api/teachers/subjects/
```

Body:

```json
{
  "name": "Mathematics",
  "description": "Math tuition",
  "icon": "calculator",
  "is_active": true
}
```

Retrieve/update/delete:

```http
GET    http://127.0.0.1:8000/api/teachers/subjects/{id}/
PATCH  http://127.0.0.1:8000/api/teachers/subjects/{id}/
DELETE http://127.0.0.1:8000/api/teachers/subjects/{id}/
```

## 9. Languages

```http
GET  http://127.0.0.1:8000/api/teachers/languages/
POST http://127.0.0.1:8000/api/teachers/languages/
```

Body:

```json
{
  "name": "Nepali",
  "code": "ne"
}
```

## 10. Teacher Profiles

Public teacher list:

```http
GET http://127.0.0.1:8000/api/teachers/profiles/
```

Useful filters:

```http
GET http://127.0.0.1:8000/api/teachers/profiles/?search=math
GET http://127.0.0.1:8000/api/teachers/profiles/?ordering=hourly_rate
GET http://127.0.0.1:8000/api/teachers/profiles/?ordering=-average_rating
```

Create teacher profile. Requires teacher Bearer token.

```http
POST http://127.0.0.1:8000/api/teachers/profiles/
```

Body:

```json
{
  "title": "Math Tutor",
  "headline": "Experienced SEE math tutor",
  "about": "I help students understand math clearly.",
  "teaching_mode": "both",
  "experience_level": "intermediate",
  "years_of_experience": 3,
  "hourly_rate": "700.00",
  "location": "Kathmandu",
  "latitude": "27.717200",
  "longitude": "85.324000",
  "service_area": 10,
  "meeting_link": "https://meet.google.com/example",
  "website": "https://example.com",
  "linkedin": "https://linkedin.com/in/example",
  "youtube": "https://youtube.com/@example",
  "is_available": true,
  "max_students": 10
}
```

Current teacher profile:

```http
GET   http://127.0.0.1:8000/api/teachers/profiles/my_profile/
PATCH http://127.0.0.1:8000/api/teachers/profiles/my_profile/
```

Teacher profile actions:

```http
POST http://127.0.0.1:8000/api/teachers/profiles/{profile_id}/add_subject/
POST http://127.0.0.1:8000/api/teachers/profiles/{profile_id}/remove_subject/
POST http://127.0.0.1:8000/api/teachers/profiles/{profile_id}/toggle_availability/
```

Add/remove subject body:

```json
{
  "subject_id": 1
}
```

## 11. Teacher Qualification, Experience, Certificate, Gallery, Availability

Requires teacher Bearer token.

Qualification:

```http
GET  http://127.0.0.1:8000/api/teachers/qualifications/
POST http://127.0.0.1:8000/api/teachers/qualifications/
```

Body:

```json
{
  "degree": "BSc Mathematics",
  "institution": "Tribhuvan University",
  "field_of_study": "Mathematics",
  "start_year": 2018,
  "end_year": 2022,
  "is_current": false,
  "description": "Focused on applied mathematics."
}
```

Experience:

```http
POST http://127.0.0.1:8000/api/teachers/experiences/
```

Body:

```json
{
  "title": "Math Teacher",
  "organization": "ABC School",
  "location": "Kathmandu",
  "start_date": "2022-01-01",
  "end_date": null,
  "is_current": true,
  "description": "Teaching secondary level mathematics."
}
```

Certificate:

```http
POST http://127.0.0.1:8000/api/teachers/certificates/
```

Body:

```json
{
  "title": "Teaching Certificate",
  "issuing_organization": "Education Board",
  "credential_id": "CERT-123",
  "credential_url": "https://example.com/cert",
  "issue_date": "2023-01-01",
  "expiry_date": null,
  "does_not_expire": true
}
```

Availability:

```http
POST http://127.0.0.1:8000/api/teachers/availability/
```

Body:

```json
{
  "day_of_week": 0,
  "start_time": "10:00:00",
  "end_time": "12:00:00",
  "is_available": true
}
```

File upload endpoints:

```http
POST http://127.0.0.1:8000/api/teachers/gallery/
POST http://127.0.0.1:8000/api/teachers/certificates/
```

In Thunder Client, set Body to `Form` or `Form-Data`, not JSON. Example gallery fields:

```txt
image: choose file
caption: Classroom session
is_primary: true
```

## 12. Student Profiles

Requires student Bearer token.

```http
GET  http://127.0.0.1:8000/api/students/profiles/
POST http://127.0.0.1:8000/api/students/profiles/
GET  http://127.0.0.1:8000/api/students/profiles/my_profile/
PATCH http://127.0.0.1:8000/api/students/profiles/my_profile/
```

Body:

```json
{
  "grade_level": "10",
  "school": "Kathmandu Model School",
  "parent_name": "Parent Name",
  "parent_phone": "9811111111",
  "parent_email": "parent@test.com",
  "learning_goals": "Improve math and science",
  "preferred_mode": "both",
  "max_budget": "800.00"
}
```

Student preferences:

```http
GET  http://127.0.0.1:8000/api/students/preferences/
POST http://127.0.0.1:8000/api/students/preferences/
```

Body:

```json
{
  "subject": 1,
  "preferred_gender": "any",
  "preferred_experience": "intermediate"
}
```

## 13. Bookings

Requires Bearer token.

List current user's bookings:

```http
GET http://127.0.0.1:8000/api/bookings/
```

Create booking. Requires student Bearer token. `teacher` is the teacher user ID, not the teacher profile ID.

```http
POST http://127.0.0.1:8000/api/bookings/
```

Body:

```json
{
  "teacher": 2,
  "subject": 1,
  "teaching_mode": "online_tuition",
  "preferred_date": "2026-07-05",
  "start_time": "10:00:00",
  "end_time": "11:00:00",
  "duration_hours": "1.00",
  "location": "Kathmandu",
  "latitude": "27.717200",
  "longitude": "85.324000",
  "student_notes": "Need help with algebra."
}
```

Booking actions:

```http
POST http://127.0.0.1:8000/api/bookings/{id}/accept/
POST http://127.0.0.1:8000/api/bookings/{id}/reject/
POST http://127.0.0.1:8000/api/bookings/{id}/cancel/
POST http://127.0.0.1:8000/api/bookings/{id}/complete/
POST http://127.0.0.1:8000/api/bookings/{id}/reschedule_request/
```

Cancel body:

```json
{
  "reason": "Schedule changed"
}
```

Reschedule request body:

```json
{
  "new_date": "2026-07-06",
  "new_start_time": "12:00:00",
  "new_end_time": "13:00:00",
  "reason": "Need a later time"
}
```

Reschedule approvals:

```http
GET  http://127.0.0.1:8000/api/bookings/reschedule-requests/
POST http://127.0.0.1:8000/api/bookings/reschedule-requests/{id}/approve/
```

## 14. Payments

Requires Bearer token.

```http
GET http://127.0.0.1:8000/api/payments/
GET http://127.0.0.1:8000/api/payments/my_transactions/
GET http://127.0.0.1:8000/api/payments/invoices/
```

Initiate payment:

```http
POST http://127.0.0.1:8000/api/payments/initiate_payment/
```

Body:

```json
{
  "booking_id": "BOOKING_ID_FROM_BOOKING_RESPONSE",
  "payment_method": "esewa"
}
```

Payment methods:

```txt
esewa
khalti
stripe
```

Verify payment:

```http
POST http://127.0.0.1:8000/api/payments/{payment_id}/verify_payment/
```

Body:

```json
{
  "transaction_id": "TXN-123456",
  "gateway_data": {
    "status": "success",
    "provider": "esewa"
  }
}
```

Refund:

```http
POST http://127.0.0.1:8000/api/payments/{payment_id}/refund/
```

Body:

```json
{
  "amount": "500.00",
  "reason": "Cancelled booking"
}
```

Webhook test endpoints:

```http
POST http://127.0.0.1:8000/api/payments/webhook/esewa/
POST http://127.0.0.1:8000/api/payments/webhook/khalti/
POST http://127.0.0.1:8000/api/payments/webhook/stripe/
```

## 15. Reviews

Requires student Bearer token for create.

```http
GET  http://127.0.0.1:8000/api/reviews/
POST http://127.0.0.1:8000/api/reviews/
```

Body:

```json
{
  "teacher": 2,
  "booking": 1,
  "rating": 5,
  "comment": "Great tutor."
}
```

## 16. Wishlist

Requires student Bearer token.

```http
GET  http://127.0.0.1:8000/api/wishlist/
POST http://127.0.0.1:8000/api/wishlist/
GET  http://127.0.0.1:8000/api/wishlist/check/?teacher_id=1
DELETE http://127.0.0.1:8000/api/wishlist/{id}/
DELETE http://127.0.0.1:8000/api/wishlist/clear/
```

Body:

```json
{
  "teacher": 1
}
```

The wishlist `teacher` field expects a teacher profile ID.

## 17. Chat

Requires Bearer token.

Create conversation:

```http
POST http://127.0.0.1:8000/api/chat/conversations/
```

Body:

```json
{
  "booking": 1,
  "participant_id": 2
}
```

List conversations:

```http
GET http://127.0.0.1:8000/api/chat/conversations/
```

Mark conversation read:

```http
POST http://127.0.0.1:8000/api/chat/conversations/{id}/mark_read/
```

Send message:

```http
POST http://127.0.0.1:8000/api/chat/messages/
```

Body:

```json
{
  "conversation": 1,
  "content": "Hello, I want to discuss the class."
}
```

Send message with file/image: use Thunder Client Form-Data.

```txt
conversation: 1
content: Here is the file.
image: choose file
file: choose file
```

Typing:

```http
POST http://127.0.0.1:8000/api/chat/typing/
```

Body:

```json
{
  "conversation": 1,
  "is_typing": true
}
```

## 18. Notifications

Requires Bearer token.

```http
GET http://127.0.0.1:8000/api/notifications/
GET http://127.0.0.1:8000/api/notifications/devices/
```

Register push device:

```http
POST http://127.0.0.1:8000/api/notifications/devices/
```

Body:

```json
{
  "device_token": "sample-device-token",
  "device_type": "web",
  "is_active": true
}
```

## 19. API Docs

Swagger UI:

```txt
http://127.0.0.1:8000/api/docs/
```

Schema:

```txt
http://127.0.0.1:8000/api/schema/
```

Redoc:

```txt
http://127.0.0.1:8000/api/redoc/
```

## Common Thunder Client Problems

Use trailing slash:

```txt
Correct: /api/auth/login/
Wrong:   /api/auth/login
```

Use unique values during registration:

```txt
email, username, phone_number
```

Use `Form-Data` for file uploads, not JSON.

If a protected endpoint returns `401`, login again and replace the Bearer token.

If teacher list is empty, approve and verify teacher users from Django Admin:

```txt
http://127.0.0.1:8000/admin/
```
