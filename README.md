# REST API for Car Park with Drivers
_REST API has been created using Django REST Framework for car park with drivers, below is a list of endpoints on which the following operations can be performed_

A list of open (without authentication) endpoints for the following operations has been created:

### Driver:
+ GET /drivers/driver/ - output of the list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output a list of drivers that are created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output a list of drivers created before 16-11-2021

+ GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
+ POST /drivers/driver/ - creating a new driver
+ UPDATE /drivers/driver/<driver_id>/ - driver editing
+ DELETE /drivers/driver/<driver_id>/ - driver deleting

## Vehicle:
+ GET /vehicles/vehicle/ - 
output of the list of cars
+ GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers

+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific car
+ POST /vehicles/vehicle/ - creating new car
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - car editing
+ POST /vehicles/set_driver/<vehicle_id>/ - put the driver in the car / get the driver out of the car
+ DELETE /vehicles/vehicle/<vehicle_id>/ - car deleting
