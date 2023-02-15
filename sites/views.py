from rest_framework import viewsets

from .models import WorldBorder
from .permissions import IsAdminUserOrReadOnly
from .serializers import WorldBorderSerializer


class WorldBorderViewSet(viewsets.ModelViewSet):
    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]

