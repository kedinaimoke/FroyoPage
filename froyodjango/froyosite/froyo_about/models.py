from django.db import models


# Create your models here.


class Main(models.Model):
    main_title = models.CharField(max_length=200)
    main_text = models.TextField()

    def __str__(self):
        return self.main_title


class SideInfo(models.Model):
    side_title = models.CharField(max_length=200)
    side_text = models.TextField()

    def __str__(self):
        return self.side_title
