# TutorConnect Nepal

A platform connecting students with teachers for home tuition and online tuition in Nepal.

## Tech Stack

- **Backend:** Python 3.12+, Django 5.0, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (SimpleJWT)
- **API Documentation:** drf-spectacular (Swagger/OpenAPI)
- **Media Storage:** Cloudinary
- **Background Tasks:** Celery + Redis
- **Real-time:** Django Channels + Redis
- **Deployment:** Docker, Docker Compose, Gunicorn, Nginx

## Features

- **Authentication:** Register, Login, JWT, Refresh Token, Logout, Change Password, Forgot/Reset Password, Email/OTP Verification, Google OAuth
- **Teachers:** Profile, Qualifications, Experience, Subjects, Languages, Hourly Rate, Location, Availability Calendar, Certificates, Gallery, Demo Video, Ratings & Reviews
- **Students:** Profile, Wishlist, Saved Teachers, Booking History, Preferences
- **Search:** Filter by Subject, Name, Price, Rating, Experience, Location, Teaching Mode, Availability
- **Bookings:** Request, Accept, Reject, Cancel, Reschedule, Status Management, Calendar Slots
- **Payments:** eSewa, Khalti, Stripe integration with webhooks
- **Reviews:** Create, Edit, Delete, Average Rating
- **Wishlist:** Add/Remove Teachers, List Saved
- **Chat:** Real-time messaging with Django Channels, Read Status, Typing Indicators
- **Notifications:** In-app, Email, Push notification structure

## Project Structure

```
tutorconnect-nepal/
├── config/                    # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   ├── wsgi.py               # WSGI configuration
│   ├── asgi.py               # ASGI configuration (Channels)
│   ├── celery.py             # Celery configuration
│   └── health.py             # Health check endpoint
├── apps/
│   ├── common/               # Shared utilities, mixins, base models
│   ├── authentication/       # JWT auth, register, login, OTP
│   ├── users/                # Custom User model, profiles
│   ├── teachers/             # Teacher profiles, subjects, availability
│   ├── students/             # Student profiles, preferences
│   ├── bookings/             # Booking system, rescheduling
│   ├── payments/             # Payment processing, webhooks
│   ├── reviews/              # Reviews and ratings
│   ├── wishlist/             # Student wishlist
│   ├── chat/                 # Real-time messaging
│   └── notifications/        # In-app and email notifications
├── nginx/
│   └── nginx.conf            # Nginx configuration
├── media/                    # Uploaded media files
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker build file
├── docker-compose.yml        # Docker Compose configuration
├── .env.example              # Environment variables template
└── README.md                 # Project documentation
```

## Installation

### Prerequisites

- Python 3.12+
- PostgreSQL
- Redis
- Docker (optional)

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd tutorconnect-nepal
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Create PostgreSQL database:**
   ```bash
   createdb tutorconnect_nepal
   ```

6. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server:**
   ```bash
   python manage.py runserver
   ```

9. **Start Celery worker (in separate terminal):**
   ```bash
   celery -A config worker -l info
   ```

## Docker Setup

```bash
# Build and run all services
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Debug mode | `True` |
| `SECRET_KEY` | Django secret key | - |
| `DB_NAME` | Database name | `tutorconnect_nepal` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `postgres` |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |
| `REDIS_URL` | Redis connection URL | `redis://localhost:6379/0` |
| `CLOUDINARY_CLOUD_NAME` | Cloudinary cloud name | - |
| `CLOUDINARY_API_KEY` | Cloudinary API key | - |
| `CLOUDINARY_API_SECRET` | Cloudinary API secret | - |
| `EMAIL_HOST_USER` | Email host user | - |
| `EMAIL_HOST_PASSWORD` | Email host password | - |
| `FRONTEND_URL` | Frontend URL | `http://localhost:3000` |

## API Documentation

Once the server is running, access the API documentation:

- **Swagger UI:** http://localhost:8000/api/docs/
- **ReDoc:** http://localhost:8000/api/redoc/
- **OpenAPI Schema:** http://localhost:8000/api/schema/

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `POST /api/auth/refresh/` - Refresh token
- `POST /api/auth/change-password/` - Change password
- `POST /api/auth/forgot-password/` - Forgot password
- `POST /api/auth/reset-password/` - Reset password
- `POST /api/auth/verify-email/` - Verify email
- `POST /api/auth/verify-otp/` - Verify OTP
- `POST /api/auth/resend-otp/` - Resend OTP
- `POST /api/auth/google/` - Google OAuth

### Users
- `GET/PUT/PATCH /api/users/me/` - Current user profile
- `GET /api/users/` - List users (admin)
- `GET /api/users/{id}/` - User detail
- `POST /api/users/{id}/approve_teacher/` - Approve teacher (admin)

### Teachers
- `GET /api/teachers/profiles/` - List teachers (with filters)
- `GET /api/teachers/profiles/{id}/` - Teacher detail
- `GET/PUT/PATCH /api/teachers/profiles/my_profile/` - My teacher profile
- `GET /api/teachers/subjects/` - List subjects
- `GET /api/teachers/languages/` - List languages
- `CRUD /api/teachers/qualifications/` - Manage qualifications
- `CRUD /api/teachers/experiences/` - Manage experiences
- `CRUD /api/teachers/certificates/` - Manage certificates
- `CRUD /api/teachers/gallery/` - Manage gallery
- `CRUD /api/teachers/availability/` - Manage availability

### Students
- `GET/PUT/PATCH /api/students/profiles/my_profile/` - My student profile
- `CRUD /api/students/preferences/` - Manage preferences

### Bookings
- `CRUD /api/bookings/` - Manage bookings
- `POST /api/bookings/{id}/accept/` - Accept booking (teacher)
- `POST /api/bookings/{id}/reject/` - Reject booking (teacher)
- `POST /api/bookings/{id}/cancel/` - Cancel booking (student)
- `POST /api/bookings/{id}/complete/` - Complete booking (teacher)
- `POST /api/bookings/{id}/reschedule_request/` - Request reschedule

### Payments
- `POST /api/payments/initiate_payment/` - Initiate payment
- `POST /api/payments/{id}/verify_payment/` - Verify payment
- `POST /api/payments/{id}/refund/` - Process refund
- `GET /api/payments/my_transactions/` - My transactions
- `POST /api/payments/webhook/esewa/` - eSewa webhook
- `POST /api/payments/webhook/khalti/` - Khalti webhook
- `POST /api/payments/webhook/stripe/` - Stripe webhook

### Reviews
- `CRUD /api/reviews/` - Manage reviews
- `GET /api/reviews/?teacher={id}` - Reviews for a teacher

### Wishlist
- `CRUD /api/wishlist/` - Manage wishlist
- `DELETE /api/wishlist/clear/` - Clear wishlist
- `GET /api/wishlist/check/?teacher_id={id}` - Check if wishlisted

### Chat
- `CRUD /api/chat/conversations/` - Manage conversations
- `CRUD /api/chat/messages/` - Manage messages
- `POST /api/chat/conversations/{id}/mark_read/` - Mark as read

### Notifications
- `GET /api/notifications/` - List notifications
- `POST /api/notifications/mark_all_read/` - Mark all read
- `GET /api/notifications/unread_count/` - Unread count
- `CRUD /api/notifications/devices/` - Push device tokens

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=apps --cov-report=html

# Run specific app tests
pytest apps/users/tests/
pytest apps/teachers/tests/
```

## Migration Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migrations
python manage.py showmigrations

# Rollback migration
python manage.py migrate <app_name> <migration_number>
```

## Admin Panel

Access the Django admin panel at `/admin/` with superuser credentials.

### Admin Features
- User management (students, teachers, admins)
- Teacher approval workflow
- Booking management
- Payment management
- Review moderation
- Subject and language management
- Analytics and reporting

## Security

- JWT authentication with token blacklisting
- Role-based permissions (Student, Teacher, Admin)
- CORS configuration
- Environment variable management
- Rate limiting
- Input validation and sanitization
- Secure password hashing
- SQL injection protection (ORM)
- XSS protection

## License

MIT License

## Support

For support, email support@tutorconnectnepal.com