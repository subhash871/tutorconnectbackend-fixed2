#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

python manage.py shell << 'PYEOF'
from apps.users.models import User

email = "rautsubhash2002@gmail.com"
password = "Subhash@20"

user, created = User.objects.get_or_create(email=email, defaults={
    "is_staff": True,
    "is_superuser": True,
    "is_active": True,
})
user.is_staff = True
user.is_superuser = True
user.is_active = True
user.set_password(password)
user.save()
print(f"Superuser ready: {email} (created={created})")
PYEOF