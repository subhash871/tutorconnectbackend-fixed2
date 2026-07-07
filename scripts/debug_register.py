import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from rest_framework.test import APIClient

client = APIClient()
data = {
    'email': 'student@example.com',
    'username': 'studuser',
    'password': 'StudPass123!',
    'password2': 'StudPass123!',
    'role': 'student',
    'phone_number': '+9771stud'
}
resp = client.post('/api/auth/register/', data, format='json')
print('status', resp.status_code)
print(resp.data)
