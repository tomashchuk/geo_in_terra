from django.contrib.auth import get_user_model
from django.contrib.gis.db import models
from django_countries.fields import CountryField
from core.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    country = CountryField()


# class Worker(BaseModel):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)


# class Site(BaseModel):
#     created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
#     company = models.ForeignKey(Company, on_delete=models.SET_NULL)
#     country = CountryField()
#
#     position = models.PointField(srid=4326)
#     geom = models.MultiPolygonField(srid=4326)


# Regular GeoDjango WorldBorder model
class WorldBorder(BaseModel):
    fips = models.CharField(max_length=2, null=True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()

    mpoly = models.MultiPolygonField(srid=4326)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
