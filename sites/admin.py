from django.contrib.gis import admin
from .models import WorldBorder, Company, Site


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', )


@admin.register(Site)
class SiteAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'company', 'country', )
    list_filter = ('company', 'country')
    search_fields = ('name', )


@admin.register(WorldBorder)
class WorldBorderAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'iso2', 'active', )
    search_fields = ('name', 'iso2', )
    list_filter = ('active', )

