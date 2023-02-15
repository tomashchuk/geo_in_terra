from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from sites.models import WorldBorder, Company, Site


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"

        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company

        fields = "__all__"


class SiteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Site
        geo_field = "position"
        bbox_geo_field = "mpoly"

        fields = "__all__"
