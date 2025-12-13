from django.db import models

# Create your models here.
from django.db import models

class Route(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.FloatField()  # in km
    
    def __str__(self):
        return f"{self.origin} → {self.destination}"
