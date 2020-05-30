from django.db import models
 
# Create your models here.
class Computer(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField()
    dpartment = models.CharField(max_length=100)
    phone = models.IntegerField()
    blood_group = models.CharField(max_length=100)

