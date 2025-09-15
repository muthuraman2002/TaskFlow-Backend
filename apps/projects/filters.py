from django_filters import rest_framework as filters
from .models import Project

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    created_by = filters.NumberFilter(field_name='created_by__id')
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Project
        fields = ['name', 'created_by', 'created_at']