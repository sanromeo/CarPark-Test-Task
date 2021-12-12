from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from carPark import views

router = routers.DefaultRouter()
router.register(r'drivers/driver', views.DriverViewSet, basename='Driver View')
router.register(r'vehicles/vehicle', views.VehicleViewSet, basename='Vehicle View')
router.register(r'vehicles/set_driver', views.SetDriverVehicleViewSet, basename='Set Driver View')
urlpatterns = [
    path('', include(router.urls))
]
