from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sites.views import WorldBorderViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'world-border', WorldBorderViewSet, basename="world_border")
router.register(r'company', CompanyViewSet, basename="company")

urlpatterns = [
    path('', include(router.urls)),
]