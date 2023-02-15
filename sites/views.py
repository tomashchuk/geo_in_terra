from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import WorldBorder, Company, Site
from .permissions import IsAdminUserOrReadOnly
from .serializers import WorldBorderSerializer, CompanySerializer, SiteSerializer
from .managers import WorldBorderManager


class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]

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
