from django.db import models
from django.utils import timezone

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=150)
    climate = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now()) #decimal do mysql
    diameter = models.DecimalField(max_digits=20, decimal_places=2)
    gravity = models.IntegerField() #int do mysql
    population = models.BigIntegerField() #bigint do mysql
    
    def __str__(self):
        return self.name
    
    
class Starships(models.Model):
    name = models.CharField(max_length=150) # varchar do mysql
    model = models.CharField(max_length=20)
    passengers = models.IntegerField() #int do mysql   
    created = models.DateTimeField(auto_now_add=True) # datetime default now() do mysql
    length = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=150) # varchar do mysql
    birthYear = models.CharField(max_length=20)
    eyeColor = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, blank=False, null=True)
    hairColor = models.CharField(max_length=50)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    mass = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True) # datetime default now() do mysql
    planet = models.ForeignKey(Planet, related_name="planet", on_delete=models.CASCADE)
    starship = models.ForeignKey(Starships, related_name="starship", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
