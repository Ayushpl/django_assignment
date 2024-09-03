import csv
import os
from django.core.management.base import BaseCommand
from trucks.models import FoodTruck
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    help = 'Load food truck data from CSV'

    def handle(self, *args, **kwargs):
        csv_path = os.path.abspath('food-truck-data.csv')
        with open(csv_path) as csvfile:
            csv_path = os.path.abspath('food-truck-data.csv')
            print(csv_path)
            reader = csv.DictReader(csvfile)
            for row in reader:
                location = Point(float(row['longitude']), float(row['latitude']))
                FoodTruck.objects.create(
                    name=row['Name'],
                    location=location,
                    address=row['Address'],
                    food_items=row['FoodItems'],
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))