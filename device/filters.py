import django_filters
from .models import device

class DeviceFilter(django_filters.FilterSet):
    other = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = device
        fields = '__all__'
        exclude = ['motherboard', 'cpu', 'ram', 'hdd', 'hdd', 'slug']