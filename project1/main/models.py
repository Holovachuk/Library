from django.db import models

# Create your models here.

class LoadImage(models.Model):
    image = models.ImageField(upload_to='images')


class LoadMultipleImages(models.Model):
    image = models.FileField(upload_to='image')