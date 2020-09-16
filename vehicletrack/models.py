from django.db import models
from django.utils import timezone
import datetime

class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=100)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return "latitude:"+str(self.latitude)+" longitude:"+str(self.longitude)+" vehicle_plate:" + str(self.vehicle) + ' datetime:'+ str(self.datetime)
