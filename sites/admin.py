from django.contrib.gis import admin
from .models import WorldBorder, Company, Site

admin.site.register(Company, admin.ModelAdmin)
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
admin.site.register(Site, admin.OSMGeoAdmin)
