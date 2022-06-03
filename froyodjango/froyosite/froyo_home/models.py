from django.db import models


# Create your models here.

class HomeEdit(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.title}"
