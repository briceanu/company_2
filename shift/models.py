from django.db import models
from driver.models import Driver
 





class Shift(models.Model):
    truck_used = models.ForeignKey('truck.Truck', on_delete=models.CASCADE,related_name='truck')
    driver_id = models.ForeignKey(Driver,on_delete=models.CASCADE,related_name='driver')
    hours_worked = models.DecimalField(max_digits=4,decimal_places=2) 
    payment_per_hour = models.DecimalField(max_digits=4,decimal_places=2)
    weight_carried = models.DecimalField(max_digits=5,decimal_places=3)
    distance_driven = models.DecimalField(max_digits=5,decimal_places=2)

    @property
    def payment_per_day(self):
        return self.hours_worked * self.payment_per_hour
    