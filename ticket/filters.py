import django_filters
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    comment = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['ticket_id', 'slug']