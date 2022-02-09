from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
    places = [
        ('C', 'Colombia'),
        ('E', 'Ecuador'),
        ('V', 'Venezuela')
    ]
 
    name = models.CharField(max_length=50)
    pob = models.CharField(max_length=1, choices=places)
    death_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(primary_key=True, max_length=100)
    author = models.ManyToManyField(Author)
    pages = models.PositiveIntegerField()
    idiom = models.CharField(max_length=20)
    editorial = models.CharField(max_length=100)

    def __str__(self):
        return self.title


