from rest_framework import viewsets
from rest_framework import permissions
from datetime import datetime as dt

from carPark.models import Driver, Vehicle
from carPark.serializers import DriverSerializer, VehicleSerializer, SetDriverSerializer


# Create your views here.


class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drivers to be viewed or edited.
    """
    serializer_class = DriverSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Driver.objects.all()
        date_gte = self.request.query_params.get('created_at__gte')
        date_lte = self.request.query_params.get('created_at__lte')
        if date_gte is not None:
            date_gte = dt.strptime(date_gte, '%d-%m-%Y')
            queryset = queryset.filter(created_at__gte=date_gte)
        elif date_lte is not None:
            date_lte = dt.strptime(date_lte, '%d-%m-%Y')
            queryset = queryset.filter(created_at__lte=date_lte)
        return queryset


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicle to be viewed or edited.
    """
    serializer_class = VehicleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'yes':
            queryset = queryset.filter(driver_id__isnull=False)
        elif with_drivers == 'no':
            queryset = queryset.filter(driver_id__isnull=True)
        return queryset


class SetDriverVehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows set driver to vehicle and unset driver from vehicle.
    """
    serializer_class = SetDriverSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Vehicle.objects.all()