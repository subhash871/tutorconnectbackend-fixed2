import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import authenticate, get_user_model
from django.test import RequestFactory
from django.contrib import admin

email = 'Subhash@gmail.com'
password = 'Subhash@2020'

user = authenticate(email=email, password=password)
print('authenticated:', bool(user))
if not user:
    User = get_user_model()
    try:
        u = User.objects.get(email__iexact=email)
        ok = u.check_password(password)
        print('found user, password ok:', ok)
        user = u if ok else None
    except User.DoesNotExist:
        user = None

if not user:
    print('Authentication failed for provided credentials')
    raise SystemExit(1)

print('is_superuser:', user.is_superuser, 'is_staff:', user.is_staff, 'role:', getattr(user, 'role', None))

rf = RequestFactory()
req = rf.get('/admin/')
req.user = user
app_list = admin.site.get_app_list(req)

out = []
for app in app_list:
    models = [m.get('name') for m in app.get('models', [])]
    out.append({'app': app.get('name'), 'models': models})

print(json.dumps(out, indent=2))
