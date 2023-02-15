from typing import Optional

from rest_framework.exceptions import ValidationError
from django.contrib.gis.geos import Point

from .models import WorldBorder


class WorldBorderManager(object):
    model_class = WorldBorder

    def get_by_geo_point(self, point_data: dict) -> Optional[WorldBorder]:
        coordinates = point_data.get("coordinates")
        point = Point(*coordinates)
        country = self.model_class.objects.filter(mpoly__intersects=point, active=True).first()

        if not country:
            raise ValidationError("Wrong coordinates or country is not supported")

        return country

