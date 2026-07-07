from django.test import TestCase, override_settings
from rest_framework.test import APIClient
from django.utils import timezone
from datetime import timedelta
from apps.users.models import User


class HappyPathTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_full_happy_path(self):
        # 1. Register teacher
        teacher_email = 'teacher1@example.com'
        resp = self.client.post('/api/auth/register/', {
            'email': teacher_email,
            'username': 'teacher1',
            'password': 'Testpass123!',
            'password2': 'Testpass123!',
            'phone_number': '1000000001',
            'role': 'teacher'
        }, format='json')
        self.assertEqual(resp.status_code, 201)
        teacher_user = User.objects.get(email__iexact=teacher_email)

        # 2. Approve teacher in admin (simulate)
        teacher_user.is_verified = True
        teacher_user.is_teacher_approved = True
        teacher_user.is_active = True
        teacher_user.save()

        # 3. Login teacher and create subject + profile
        resp = self.client.post('/api/auth/login/', {'email': teacher_email, 'password': 'Testpass123!'}, format='json')
        self.assertEqual(resp.status_code, 200)
        teacher_token = resp.data['data']['tokens']['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {teacher_token}')

        # create subject
        resp = self.client.post('/api/teachers/subjects/', {'name': 'Mathematics'}, format='json')
        self.assertIn(resp.status_code, (200, 201))
        subject_id = resp.data.get('id')

        # create teacher profile
        profile_payload = {'title': 'Senior Math Tutor', 'hourly_rate': '20.00', 'teaching_mode': 'online_tuition', 'is_available': True}
        resp = self.client.post('/api/teachers/profiles/', profile_payload, format='json')
        self.assertIn(resp.status_code, (200, 201))
        teacher_profile_id = resp.data.get('id')

        # add subject to profile
        resp = self.client.post(f'/api/teachers/profiles/{teacher_profile_id}/add_subject/', {'subject_id': subject_id}, format='json')
        self.assertEqual(resp.status_code, 200)

        # 4. Register student
        student_email = 'student1@example.com'
        resp = self.client.post('/api/auth/register/', {
            'email': student_email,
            'username': 'student1',
            'password': 'Testpass123!',
            'password2': 'Testpass123!',
            'phone_number': '1000000002',
            'role': 'student'
        }, format='json')
        self.assertEqual(resp.status_code, 201)
        student_user = User.objects.get(email__iexact=student_email)
        student_user.is_verified = True
        student_user.is_active = True
        student_user.save()

        # 5. Login student and create profile
        resp = self.client.post('/api/auth/login/', {'email': student_email, 'password': 'Testpass123!'}, format='json')
        self.assertEqual(resp.status_code, 200)
        student_token = resp.data['data']['tokens']['access']
        student_client = APIClient()
        student_client.credentials(HTTP_AUTHORIZATION=f'Bearer {student_token}')

        # create student profile via my_profile
        resp = student_client.put('/api/students/profiles/my_profile/', {'grade_level': '10', 'school': 'Central High'}, format='json')
        self.assertIn(resp.status_code, (200, 201))

        # 6. Student books teacher
        preferred_date = (timezone.now() + timedelta(days=1)).date().isoformat()
        booking_payload = {
            'teacher': teacher_user.id,
            'subject': subject_id,
            'teaching_mode': 'online_tuition',
            'preferred_date': preferred_date,
            'start_time': '10:00:00',
            'end_time': '11:00:00',
            'duration_hours': '1.00',
            'location': 'Online'
        }
        resp = student_client.post('/api/bookings/', booking_payload, format='json')
        self.assertEqual(resp.status_code, 201)
        booking_id = resp.data['id']
        booking_booking_id = resp.data['booking_id']

        # 7. Teacher accepts booking
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {teacher_token}')
        resp = self.client.post(f'/api/bookings/{booking_id}/accept/', format='json')
        self.assertEqual(resp.status_code, 200)

        # 8. Student initiates payment
        resp = student_client.post('/api/payments/initiate_payment/', {'booking_id': booking_booking_id, 'payment_method': 'stripe'}, format='json')
        self.assertEqual(resp.status_code, 201)
        payment_id = resp.data['id']

        # verify payment (simulate)
        resp = student_client.post(f'/api/payments/{payment_id}/verify_payment/', {'transaction_id': 'TX12345', 'gateway_data': {}}, format='json')
        self.assertEqual(resp.status_code, 200)

        # 9. Student leaves review
        review_payload = {'teacher': teacher_profile_id, 'booking': booking_id, 'rating': 5, 'comment': 'Great session!'}
        resp = student_client.post('/api/reviews/', review_payload, format='json')
        self.assertEqual(resp.status_code, 201)

        # 10. Chat between student and teacher
        resp = student_client.post('/api/chat/conversations/', {'participant_id': teacher_user.id}, format='json')
        self.assertIn(resp.status_code, (200, 201))
        conv_id = resp.data.get('id')

        # student sends message
        resp = student_client.post('/api/chat/messages/', {'conversation': conv_id, 'content': 'Hello, looking forward to our class.'}, format='json')
        self.assertEqual(resp.status_code, 201)

        # teacher fetches messages
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {teacher_token}')
        resp = self.client.get(f'/api/chat/messages/?conversation={conv_id}')
        self.assertEqual(resp.status_code, 200)
        messages = resp.data
        self.assertTrue(len(messages) >= 1)
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from apps.users.models import User
from apps.bookings.models import Booking


class HappyPathTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base = '/api'
        self._phone_seq = 1000

    def register(self, email, username, password, role='student'):
        url = f'{self.base}/auth/register/'
        data = {
            'email': email,
            'username': username,
            'password': password,
            'password2': password,
            'role': role,
            'phone_number': f'+9771{username[-4:]}'
        }
        data['phone_number'] = f'+9771{self._phone_seq}'
        self._phone_seq += 1
        return self.client.post(url, data, format='json')

    def login(self, email, password):
        url = f'{self.base}/auth/login/'
        resp = self.client.post(url, {'email': email, 'password': password}, format='json')
        return resp

    def auth_client(self, access_token):
        c = APIClient()
        c.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        return c

    def test_full_happy_path(self):
        # 1. Register teacher
        teacher_email = 'teacher@example.com'
        teacher_pass = 'TeachPass123!'
        r = self.register(teacher_email, 'teachuser', teacher_pass, role='teacher')
        self.assertEqual(r.status_code, 201)

        # 2. Approve teacher in admin (simulate by setting flag)
        teacher = User.objects.get(email=teacher_email)
        teacher.is_teacher_approved = True
        teacher.is_verified = True
        teacher.save()

        # 3. Create teacher profile and subject
        login_resp = self.login(teacher_email, teacher_pass)
        self.assertEqual(login_resp.status_code, 200)
        access = login_resp.data.get('data', {}).get('tokens', {}).get('access')
        teacher_client = self.auth_client(access)

        # create a subject
        sub_resp = teacher_client.post(f'{self.base}/teachers/subjects/', {'name': 'Mathematics'}, format='json')
        self.assertIn(sub_resp.status_code, (200, 201))
        subject_id = sub_resp.data.get('id')

        # create teacher profile (hourly_rate required)
        prof_resp = teacher_client.post(
            f'{self.base}/teachers/profiles/',
            {'title': 'Math Tutor', 'hourly_rate': '15.00', 'is_available': True},
            format='json'
        )
        self.assertIn(prof_resp.status_code, (200, 201))
        # fetch my_profile to obtain id (create returns no id in this serializer)
        my_prof = teacher_client.get(f'{self.base}/teachers/profiles/my_profile/')
        self.assertEqual(my_prof.status_code, 200)
        profile_id = my_prof.data.get('id')

        # add subject to profile
        add_sub = teacher_client.post(f'{self.base}/teachers/profiles/{profile_id}/add_subject/', {'subject_id': subject_id}, format='json')
        self.assertEqual(add_sub.status_code, 200)

        # 4. Register student
        student_email = 'student@example.com'
        student_pass = 'StudPass123!'
        r = self.register(student_email, 'studuser', student_pass, role='student')
        if r.status_code != 201:
            print('Register student response:', r.status_code, r.data)
        self.assertEqual(r.status_code, 201)

        # 5. Create student profile
        login_resp = self.login(student_email, student_pass)
        self.assertEqual(login_resp.status_code, 200)
        s_access = login_resp.data.get('data', {}).get('tokens', {}).get('access')
        student_client = self.auth_client(s_access)

        stu_prof = student_client.put(f'{self.base}/students/profiles/my_profile/', {'grade_level': '10', 'school': 'Local High'}, format='json')
        self.assertIn(stu_prof.status_code, (200, 201))

        # 6. Student books teacher
        book_data = {
            'teacher': teacher.id,
            'subject': subject_id,
            'teaching_mode': 'online_tuition',
            'preferred_date': '2026-07-10',
            'start_time': '10:00:00',
            'end_time': '11:00:00',
            'duration_hours': '1.00'
        }
        book_resp = student_client.post(f'{self.base}/bookings/', book_data, format='json')
        if book_resp.status_code != 201:
            print('Booking response:', book_resp.status_code, book_resp.data)
        self.assertEqual(book_resp.status_code, 201)
        # creation response uses BookingCreateSerializer (no id), so fetch created booking from DB
        booking_obj = Booking.objects.filter(student__email=student_email).first()
        if not booking_obj:
            print('No booking found in DB; response:', book_resp.data)
        self.assertIsNotNone(booking_obj)
        booking_id = booking_obj.id

        # 7. Teacher accepts booking
        accept_resp = teacher_client.post(f'{self.base}/bookings/{booking_id}/accept/', format='json')
        self.assertEqual(accept_resp.status_code, 200)
        booking_obj.refresh_from_db()
        self.assertEqual(booking_obj.status, 'accepted')

        # 8. Student initiates payment
        pay_resp = student_client.post(f'{self.base}/payments/initiate_payment/', {'booking_id': booking_obj.booking_id, 'payment_method': 'stripe'}, format='json')
        self.assertEqual(pay_resp.status_code, 201)
        payment_id = pay_resp.data.get('id')

        # verify payment (simulate gateway - no real Stripe/eSewa/Khalti creds
        # are configured in tests, so this exercises the DEBUG-only manual
        # confirmation fallback rather than a real gateway call)
        with override_settings(DEBUG=True):
            verify_resp = student_client.post(
                f'{self.base}/payments/{payment_id}/verify_payment/',
                {'transaction_id': 'TX12345', 'gateway_data': {'status': 'success'}},
                format='json',
            )
        self.assertEqual(verify_resp.status_code, 200)
        booking_obj.refresh_from_db()
        self.assertTrue(booking_obj.is_paid)

        # 8b. Teacher marks the session complete (reviews now require this)
        complete_resp = teacher_client.post(f'{self.base}/bookings/{booking_id}/complete/', format='json')
        self.assertEqual(complete_resp.status_code, 200)
        booking_obj.refresh_from_db()
        self.assertEqual(booking_obj.status, 'completed')

        # 9. Student leaves review
        review_resp = student_client.post(f'{self.base}/reviews/', {'teacher': profile_id, 'booking': booking_obj.id, 'rating': 5, 'comment': 'Great session!'}, format='json')
        self.assertEqual(review_resp.status_code, 201)

        # 10. Chat between student and teacher
        conv_resp = student_client.post(f'{self.base}/chat/conversations/', {'participant_id': teacher.id}, format='json')
        self.assertIn(conv_resp.status_code, (200, 201))
        conv_id = conv_resp.data.get('id')

        msg_resp = student_client.post(f'{self.base}/chat/messages/', {'conversation': conv_id, 'content': 'Hello, looking forward to our class.'}, format='json')
        self.assertEqual(msg_resp.status_code, 201)

        # teacher sends reply
        msg2 = teacher_client.post(f'{self.base}/chat/messages/', {'conversation': conv_id, 'content': 'Thanks, see you then.'}, format='json')
        self.assertEqual(msg2.status_code, 201)
