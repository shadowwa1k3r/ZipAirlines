from django.db import models

class Airplane(models.Model):
    airplane_id = models.IntegerField()
    passenger_count = models.IntegerField()

    class Meta:
        db_table = 'airplane'
    
    def __str__(self):
        return 'airplane ' + str(self.airplane_id)