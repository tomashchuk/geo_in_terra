from django.db.models import Q
from rest_framework import filters
from rest_framework.exceptions import ParseError

from django.contrib.gis.geos import Point


class IsOwnerFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(created_by=request.user)


class CountryIsoFilter(filters.BaseFilterBackend):
    country_code_param = 'country_code'

    def get_filter_country_code(self, request, **kwargs):
        country_code_string = request.query_params.get(self.country_code_param, None)
        if not country_code_string:
            return None
        return country_code_string

    def filter_queryset(self, request, queryset, view):
        country_code = self.get_filter_country_code(request)
        if not country_code:
            return queryset

        return queryset.filter(country__iso2__iexact=country_code)


class PolygonContainsFilter(filters.BaseFilterBackend):
    coordinates_param = 'polygon_contains'

    def get_filter_point(self, request, **kwargs):
        coordinates_string = request.query_params.get(self.coordinates_param, None)
        if not coordinates_string:
            return None

        try:
            (x, y) = (float(n) for n in coordinates_string.split(','))
        except ValueError:
            raise ParseError(
                'Invalid geometry string supplied for parameter {0}'.format(
                    self.coordinates_param
                )
            )

        return Point(x, y, **kwargs)

    def filter_queryset(self, request, queryset, view):
        filter_field = getattr(view, 'polygon_contains_filter_field', None)

        if not filter_field:
            return queryset

        point = self.get_filter_point(request)
        if not point:
            return queryset

        field_lookup = f'{filter_field}__intersects'
        return queryset.filter(
            Q(**{field_lookup: point})
        )
