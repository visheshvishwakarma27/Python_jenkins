from pyexpat import model
from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name=models.CharField(max_length=30)
    contact=models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    


