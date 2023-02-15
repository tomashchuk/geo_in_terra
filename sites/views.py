from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import WorldBorder, Company, Site
from .permissions import IsAdminUserOrReadOnly
from .serializers import WorldBorderSerializer, CompanySerializer, SiteSerializer


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
