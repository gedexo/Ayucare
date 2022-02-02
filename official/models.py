from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.urls import reverse


class DistrictMap(models.Model):
    name       = models.CharField(max_length=255,unique=True)
    latitude   = models.CharField(max_length=255)
    longitude  = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Branch(models.Model):
    name       = models.CharField(max_length=255,unique=True)
    title      = models.CharField(max_length=255,unique=True)
    phone      = models.CharField(max_length=10)
    location   = models.CharField(max_length=255)
    latitude   = models.CharField(max_length=255)
    longitude  = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = ('Branches')

    def __str__(self):
        return str(self.name)

class Doctor(models.Model):
    register_number =models.IntegerField(unique=True)
    name = models.CharField(max_length=128)
    image = VersatileImageField(upload_to ='doctors',blank=True,null=True)
    qualification = models.CharField(max_length=128)
    
    def __str__(self):
        return str(self.name)


class Schedule(models.Model):


    treatment = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch,on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    start_time = models.TimeField(max_length=100)
    end_time = models.TimeField(max_length=100)

   

    def __str__(self):
        return str(self.treatment)