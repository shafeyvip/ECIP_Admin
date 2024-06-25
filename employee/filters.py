import django_filters
from .models import employee

class EmployeeFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(lookup_expr='icontains')
    employee_phone_1 = django_filters.CharFilter(lookup_expr='icontains')
    employee_email = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = employee
        fields = '__all__'
        exclude = ['image', 'slug', 'employee_phone_2']