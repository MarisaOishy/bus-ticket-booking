from bookings.models import Booking
from buses.models import Seat

def get_available_seats(schedule):
    booked_seats = Booking.objects.filter(
        schedule=schedule
    ).values_list('seat_id', flat=True)

    return Seat.objects.exclude(id__in=booked_seats)
