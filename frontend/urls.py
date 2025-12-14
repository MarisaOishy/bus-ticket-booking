from django.urls import path
from .views import search_bus, select_seat

urlpatterns = [
    path('', search_bus, name='search_bus'),
    path('seats/<int:schedule_id>/', select_seat, name='select_seat'),
]
