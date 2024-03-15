from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 16)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Team(models.Model):
    name = models.CharField(max_length = 32)
    description = models.TextField()
    country = models.CharField(max_length = 32)
    sport = models.CharField(max_length = 16)

    def __str__(self):
        return self.name

class Kit(models.Model):
    name = models.CharField(max_length = 64)
    description = models.TextField()
    picture = models.URLField()
    year = models.DecimalField(max_digits = 4, decimal_places = 0)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    size = models.CharField(max_length=64)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_kits")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_kits")