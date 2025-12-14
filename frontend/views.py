from django.shortcuts import render, get_object_or_404
from schedules.models import Schedule
from buses.models import Seat

def search_bus(request):
    schedules = Schedule.objects.all()
    return render(request, 'search_bus.html', {'schedules': schedules})

def select_seat(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    seats = Seat.objects.filter(bus=schedule.bus)
    return render(request, 'select_seat.html', {
        'schedule': schedule,
        'seats': seats
    })
