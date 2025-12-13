from django.urls import path
from .views import search_bus

urlpatterns = [
    path('', search_bus, name='search_bus'),
    path('', include('frontend.urls')),

]
