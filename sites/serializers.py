from rest_framework_gis.serializers import GeoFeatureModelSerializer

from sites.models import WorldBorder


class WorldBorderSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = WorldBorder
        geo_field = "mpoly"

        fields = "__all__"
