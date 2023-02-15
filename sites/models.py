from django.contrib.auth import get_user_model
from django.contrib.gis.db import models
from django_countries.fields import CountryField
from core.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=100)
    country = CountryField()


# Regular GeoDjango WorldBorder model. Filled from helpers.data
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


class Site(BaseModel):

    class Status(models.TextChoices):
        TODO = 'todo', 'To Do'
        IN_PROGRESS = 'in_progress', 'In Progress'
        READY_FOR_REVIEW = 'ready_for_review', 'Ready For Review'
        DONE = 'done', 'Done'
        FROZEN = 'frozen', 'Frozen'

    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(WorldBorder, on_delete=models.PROTECT)

    position = models.PointField(srid=4326)
    mpoly = models.MultiPolygonField(srid=4326, null=True)

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.TODO,
    )

