from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length = 64, null = True) 
  contact_email = models.CharField(max_length=64, null = True) 
  Major = models.CharField(max_length=64)
  CourseNumber = models.IntegerField(null = True)
  has_group1 = models.BooleanField(default = False)
  time_management = models.CharField(max_length = 64, null = True) 
  time_zone = models.CharField(max_length = 64, null = True) 
  in_person = models.BooleanField(default = False)