from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  last_name = models.CharField(max_length = 64, null = True) 
  contact_email = models.CharField(max_length=64, null = True) 
  Course1 = models.CharField(max_length=64)
  has_group1 = models.BooleanField(default = False)
  