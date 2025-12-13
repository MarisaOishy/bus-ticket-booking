from django.db import models
from django.contrib.auth.models import User
from schedules.models import Schedule
from buses.models import Seat


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )
    seat = models.ForeignKey(
        Seat,
        on_delete=models.CASCADE
    )
    booking_time = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        # Prevent same seat being booked twice for the same schedule
        unique_together = ('schedule', 'seat')

    def __str__(self):
        return f"{self.user.username} | {self.schedule} | Seat {self.seat.seat_number}"
