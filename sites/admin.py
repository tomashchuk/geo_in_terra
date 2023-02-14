from django.contrib.gis import admin
from .models import WorldBorder, Company

admin.site.register(Company, admin.ModelAdmin)
