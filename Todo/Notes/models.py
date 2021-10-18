from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    createdOn = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
