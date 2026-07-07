import random
import string
from django.utils import timezone
from datetime import timedelta


def generate_otp(length=6):
    """
    Generate a numeric OTP of specified length.
    """
    return ''.join(random.choices(string.digits, k=length))


def generate_reference_id(prefix='TCN'):
    """
    Generate a unique reference ID for bookings, payments, etc.
    Format: TCN-YYYYMMDD-XXXXXXXX
    """
    import uuid
    date_part = timezone.now().strftime('%Y%m%d')
    unique_part = uuid.uuid4().hex[:8].upper()
    return f'{prefix}-{date_part}-{unique_part}'


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two coordinates using the Haversine formula.
    Returns distance in kilometers.
    """
    import math
    
    R = 6371  # Earth's radius in kilometers
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c


def get_client_ip(request):
    """
    Get the client IP address from the request.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def format_currency(amount, currency='NPR'):
    """
    Format amount with currency symbol.
    """
    symbols = {
        'NPR': 'Rs.',
        'USD': '$',
        'INR': '₹',
    }
    symbol = symbols.get(currency, 'Rs.')
    return f'{symbol} {amount:,.2f}'


def get_time_slots(start_time, end_time, interval_minutes=60):
    """
    Generate time slots between start and end time.
    """
    slots = []
    current = start_time
    while current < end_time:
        slot_end = (timezone.datetime.combine(timezone.now().date(), current) + 
                    timedelta(minutes=interval_minutes)).time()
        slots.append({
            'start': current.strftime('%H:%M'),
            'end': slot_end.strftime('%H:%M')
        })
        current = slot_end
    return slots