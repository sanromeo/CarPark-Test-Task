from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=64)
    last_name = models.CharField(verbose_name='Last Name', max_length=64)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.CharField(verbose_name='Make of car', max_length=32)
    model = models.CharField(verbose_name='Model of car', max_length=64)

    plate_number = models.CharField(verbose_name='Plate number', max_length=10,
                                    validators=[RegexValidator("[A-ZА-Я]{2}\s\d{4}\s[A-ZА-Я]{2}")],
                                    unique=True)
                                    # format example "AA 1234 OO"
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
