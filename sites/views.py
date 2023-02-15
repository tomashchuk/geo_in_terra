from rest_framework import viewsets

from .models import WorldBorder, Company
from .permissions import IsAdminUserOrReadOnly
from .serializers import WorldBorderSerializer, CompanySerializer


class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUserOrReadOnly, ]
