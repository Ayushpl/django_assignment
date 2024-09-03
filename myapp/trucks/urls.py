from django.urls import path
from views import NearbyFoodTrucks

urlpatterns = [
    path('nearby/', NearbyFoodTrucks.as_view(), name='nearby-food-trucks'),
]