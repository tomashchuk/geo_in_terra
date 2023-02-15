from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from sites.models import WorldBorder, Company


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"

        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
