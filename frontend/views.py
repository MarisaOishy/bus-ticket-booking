from django.shortcuts import render
from routes.models import Route
from schedules.models import Schedule

def search_bus(request):
    routes = Route.objects.all()
    schedules = None

    if request.method == "POST":
        route_id = request.POST.get('route')
        date = request.POST.get('date')
        schedules = Schedule.objects.filter(
            route_id=route_id,
            date=date
        )

    return render(request, 'frontend/search.html', {
        'routes': routes,
        'schedules': schedules
    })
