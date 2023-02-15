from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sites.views import WorldBorderViewSet

router = DefaultRouter()
router.register(r'world-border', WorldBorderViewSet, basename="world_border")

urlpatterns = [
    path('', include(router.urls)),
]