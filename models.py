from unicodedata import name
from django.db import models

def Passenger(models.Model):
    name=models.CharField(max_lenght=40)
    last_name=models.CharField(max_lenght=40)
    
def BusCompany(models.Model):
    name=models.CharField(max_lenght=40)
    destinations=models.CharField(max_lenght=40)

def BusInfo(model.Model):
    seats=models.BooleamField()
    seat_type=models.CharField(max_lenght=40)


