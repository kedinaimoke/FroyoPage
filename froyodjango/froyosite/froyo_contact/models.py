from django.db import models
from shortuuidfield import ShortUUIDField


# Create your models here.

class Address(models.Model):
    address = models.CharField(max_length=200)
    mail_box = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class MessageBox(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return f"{self.email} | {self.uuid}"
