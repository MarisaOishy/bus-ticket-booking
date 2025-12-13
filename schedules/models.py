from django.db import models

# Create your models here.
from django.db import models
from buses.models import Bus
from routes.models import Route

class Schedule(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.bus} | {self.route} | {self.departure_time}"
