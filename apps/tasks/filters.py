from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    assigned_user = filters.CharFilter(field_name='assigned_user__username', lookup_expr='icontains')
    deadline = filters.DateFilter()
    priority = filters.ChoiceFilter(choices=Task.PRIORITY_CHOICES)
    status = filters.ChoiceFilter(choices=Task.STATUS_CHOICES)
    project = filters.CharFilter(field_name='project__name', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['title', 'assigned_user', 'deadline', 'priority', 'status', 'project']