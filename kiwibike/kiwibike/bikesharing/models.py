from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=120)


class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=120)


class Station(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=120)
    free_bikes = models.IntegerField(default=0)