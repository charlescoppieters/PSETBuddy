from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length = 64, null = True) #same for this one
  contact_email = models.CharField(max_length=64, null = True) #did this to run, so added a default value 
  origination = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  taking_passengers = models.BooleanField(default=False)
  wants_totalk = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)
