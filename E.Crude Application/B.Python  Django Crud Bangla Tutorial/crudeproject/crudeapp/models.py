from django.db import models

# Create your models here.

class inserting(models.Model):
    name = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    age = models.CharField(max_length=30)