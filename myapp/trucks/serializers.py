from rest_framework import serializers
from models import FoodTruck

class FoodTruckSerializer(serializers.ModelSerializer):
    distance = serializers.SerializerMethodField()

    class Meta:
        model = FoodTruck
        fields = ['name',
                  'location',
                  'address',
                  'food_items', 
                  'distance'
                 ]

    def get_distance(self, obj):
        return obj.distance.km if hasattr(obj, 'distance') else None
