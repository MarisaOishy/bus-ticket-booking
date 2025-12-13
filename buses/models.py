from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20, unique=True)
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.bus_number})"


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.bus.bus_number} - Seat {self.seat_number}"

