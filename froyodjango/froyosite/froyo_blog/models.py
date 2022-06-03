from django.db import models


# Create your models here.

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=60)
    text = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.title}"
