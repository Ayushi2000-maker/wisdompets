from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    
    name = models.CharField(max_lenght=100)
    submitter = models.CharField(max_lenght=100)
    species = models.CharField(max_lenght=50)
    breed = models.CharField(max_lenght=50, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submisssion_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)
    
class Vaccine(models.Model):
    name = models.CharField(max_length=50)