
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework.response import Response
from rest_framework.views import APIView
from models import FoodTruck
from serializers import FoodTruckSerializer

class NearbyFoodTrucks(APIView):

    def get(self, request, *args, **kwargs):
        latitude = float(request.query_params.get('latitude'))
        longitude = float(request.query_params.get('longitude'))
        user_location = Point(longitude, latitude, srid=4326)
        
        # Find the nearest food trucks
        trucks = FoodTruck.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')[:5]

        serializer = FoodTruckSerializer(trucks, many=True)
        return Response(serializer.data)