from django.db import models


# Create your models here.

class Group(models.Model):
    group = models.CharField(max_length=200)
    group_desc = models.TextField()

    def __str__(self):
        return self.group


class Flavour(models.Model):
    flavour_name = models.CharField(max_length=50)
    flavour_image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.flavour_name
