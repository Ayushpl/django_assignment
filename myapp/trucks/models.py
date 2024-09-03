
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class FoodTruck(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(default=Point())
    address = models.TextField()
    food_items = models.TextField()

    def __str__(self):
        return self.name
