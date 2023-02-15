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
    created_by = serializers.CharField(source='created_by.id', read_only=True)
    updated_by = serializers.CharField(source='updated_by.id', read_only=True, allow_null=True)
    country = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Site
        geo_field = "position"
        bbox_geo_field = "mpoly"

        fields = "__all__"
