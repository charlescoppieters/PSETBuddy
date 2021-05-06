from django.db import models
from datetime import datetime


# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length = 64, null = True) 
  contact_email = models.CharField(max_length=64, null = True) 
  Major = models.CharField(max_length=64)
  CourseNumber = models.IntegerField(null = True)
  has_group1 = models.BooleanField(default = False)
  time_management = models.IntegerField(null=True)
  time_zone = models.IntegerField(null=True)
  zoom_preference = models.IntegerField(null=True)
  date = models.DateTimeField(auto_now=True)

class Feedback(models.Model):
  first_name = models.CharField(max_length=64, null = True)
  last_name = models.CharField(max_length=64, null = True)
  email = models.CharField(max_length=64, null = True)
  feedback = models.CharField(max_length=256, null = True)