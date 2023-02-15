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

    def perform_create(self, serializer):
        country = WorldBorderManager().get_by_geo_point(serializer.initial_data.get("position"))
        serializer.save(created_by=self.request.user, country=country)
