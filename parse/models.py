from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Country(models.Model):
    name = models.CharField(max_length=150, unique=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
