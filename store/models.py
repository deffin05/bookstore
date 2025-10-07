from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    publisher = models.ForeignKey('Publisher', on_delete=models.PROTECT)
    pages = models.IntegerField()
    year = models.IntegerField()
    available = models.BooleanField()


class Author(models.Model):
    name = models.CharField(max_length=100)

class Publisher(models.Model):
    name = models.CharField(max_length=100)
