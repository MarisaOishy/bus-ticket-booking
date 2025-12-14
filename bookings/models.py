from django.db import models
from django.contrib.auth.models import User
from schedules.models import Schedule
from buses.models import Seat

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    total_fare = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default='CONFIRMED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id}"
