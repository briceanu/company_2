from django.db import models




class Truck(models.Model):
    truck_brand = models.CharField(max_length=20)
    truck_model = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20) 


    