from django.contrib.gis.db import models
from django_countries.fields import CountryField


class Company(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
