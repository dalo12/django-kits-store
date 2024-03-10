from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 16)
    description = models.TextField()

class Team(models.Model):
    name = models.charField(max_length = 32)
    description = models.TextField()
    country = models.charField(max_length = 32)
    sport = models.charField(max_length = 16)

class Kit(models.Model):
    picture = models.URLField()
    name = models.CharField(max_length = 64)
    year = models.DecimalField(max_digits = 4, decimal_places = 0)
    price = models.DecimalField(decimal_places = 2)
    size = models.CharField()
    description = models.TextField()