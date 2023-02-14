from django.contrib.gis.db import models
from django_countries.fields import CountryField

from core.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    country = CountryField()
