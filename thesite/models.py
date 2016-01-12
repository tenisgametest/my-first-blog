from django.db import models
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=200)
    age = models.IntegerField()
    shortbio = models.TextField()

    def __str__(self):
        return self.name
