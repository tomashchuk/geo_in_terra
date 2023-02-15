from rest_framework.routers import DefaultRouter
from sites.views import WorldBorderViewSet, CompanyViewSet, SiteViewSet

router = DefaultRouter()
router.register(r'construction-site', SiteViewSet, basename="site")
router.register(r'world-border', WorldBorderViewSet, basename="world_border")
router.register(r'company', CompanyViewSet, basename="company")
