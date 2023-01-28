from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    code = models.CharField(primary_key=True, max_length=100, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    checkin_date = models.DateField(default=timezone.now)
    checkout_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Rate(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    allotment = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price)
