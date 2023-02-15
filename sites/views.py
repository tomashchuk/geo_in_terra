from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_gis.filters import DistanceToPointOrderingFilter
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from .filters import CountryIsoFilter, PolygonContainsFilter
from .models import WorldBorder, Company, Site
from .permissions import IsAdminUserOrReadOnly
from .serializers import WorldBorderSerializer, CompanySerializer, SiteSerializer
from .managers import WorldBorderManager


class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]

    filter_backends = (PolygonContainsFilter, DjangoFilterBackend, SearchFilter)
    polygon_contains_filter_field = 'mpoly'
    search_fields = ('name', )
    filterset_fields = ('active', )


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUserOrReadOnly, ]

    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', )
    filterset_fields = ('country', )


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]

    # DistanceToPointFilter - filters a queryset to only those instances within a certain distance of a given point
    # CountryIsoFilter - filters by iso2 of country
    # PolygonContainsFilter - filters by point in polygon
    distance_filter_field = 'position'
    polygon_contains_filter_field = 'mpoly'
    filter_backends = (
        DistanceToPointOrderingFilter,
        PolygonContainsFilter,
        CountryIsoFilter,
        DjangoFilterBackend,
        SearchFilter
    )

    search_fields = ('name', )
    filterset_fields = ('status', )

    def _get_country(self, serializer):
        return WorldBorderManager().get_by_geo_point(serializer.initial_data.get("position"))

    def perform_create(self, serializer):
        country = self._get_country(serializer)
        serializer.save(created_by=self.request.user, country=country)

    def perform_update(self, serializer):
        if serializer.initial_data.get("position"):
            country = self._get_country(serializer)
            serializer.save(updated_by=self.request.user, country=country)
            return
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance: Site):
        if instance.created_by.id == self.request.user.id:
            instance.delete()
            return

        raise ValidationError("You cannot delete this construction site. Ask the creator to do this")
