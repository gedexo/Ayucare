from django.db import models
from datetime import *
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField


class Treatment(models.Model):
    
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    image = VersatileImageField(upload_to = "Treatment")
    image1 = VersatileImageField(upload_to = "Treatment")
    image2 = VersatileImageField(upload_to = "Treatment")
    image3 = VersatileImageField(upload_to = "Treatment")
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class Subscribe(models.Model):
    email = models.EmailField(max_length=128)

    def __str__(self):
        return str(self.email)


class Gallery(models.Model):
    image = VersatileImageField(upload_to ="Galleries")

    class Meta:
        verbose_name_plural = ('Gallery')

    def __str__(self):
        return str(self.image)

class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    text = models.TextField()

    def __str__(self):
        return str(self.name)

class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    image = VersatileImageField(upload_to ="Testimonial")
    text = models.TextField()

    def __str__(self):
        return str(self.name)






