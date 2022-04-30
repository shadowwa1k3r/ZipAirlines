from django.db import models
from math import log10

class Airplane(models.Model):
    airplane_id = models.IntegerField()
    passenger_count = models.IntegerField()
    fuel_tank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'airplane'
    
    def __str__(self):
        return 'airplane ' + str(self.airplane_id)

    @property
    def fuel_consumption_per_minute(self):
        """
        calculate fuel consumption
        """
        return log10(self.airplane_id*0.80)+self.passenger_count*0.002

    @property
    def flight_time(self):
        """
        calculate flight time
        """
        return self.fuel_tank/self.fuel_consumption_per_minute

    def save(self, *args, **kwargs):
        self.fuel_tank = 200*self.airplane_id
        super(Airplane, self).save(*args, **kwargs)
        
        