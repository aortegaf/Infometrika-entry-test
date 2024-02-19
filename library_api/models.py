from django.db import models
from django.contrib.auth.models import AbstractUser

class Writer(models.Model):
    places = [
        ('C', 'Colombia'),
        ('E', 'Ecuador'),
        ('V', 'Venezuela')
    ]
 
    name = models.CharField(max_length=50)
    nacionality = models.CharField(max_length=1, choices=places)
    death_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(primary_key=True, max_length=100)
    writer = models.ManyToManyField(Writer)
    pages = models.PositiveIntegerField()
    language = models.CharField(max_length=20)
    editorial = models.CharField(max_length=100)

    def __str__(self):
        return self.title


