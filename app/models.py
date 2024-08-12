from django.db import models
from django.contrib.auth.models import User #principal model
import datetime
from  django.utils.timezone import now


# Create your models here.
class bus(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=50)
    bus_number=models.CharField(max_length=10)
    start=models.CharField(max_length=50)
    end=models.CharField(max_length=50)
    date=models.DateTimeField(default=now())

    def __str__(self):
        return f'{self.username} books {self.bus_number}' #fstring to get raw data
    


