from django.db import models

# Create your models here.

class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.CharField(max_length=128, unique=False, null=True)
    diameter = models.IntegerField(unique=False, null=True)
    orbital_period = models.IntegerField(unique=False, null=True)
    population = models.BigIntegerField(unique=False, null=True)
    rotation_period = models.IntegerField(unique=False, null=True)
    surface_water = models.FloatField(unique=False, null=True)
    terrain = models.CharField(max_length=128, unique=False, null=True)
    created = models.DateTimeField(auto_now_add=True, unique=False, null=True)
    updated = models.DateTimeField(auto_now=True, unique=False, null=True)
    def __str__(self) -> str:
        return self.name
    
class People(models.Model):
    name = models.CharField(max_length=64, null=True)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    homeworld = models.ForeignKey(Planets,on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name


    