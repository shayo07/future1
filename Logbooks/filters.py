import django_filters
from .models import *
from django_filters import CharFilter

class LogBookSFilter(django_filters.FilterSet):
    log_name=CharFilter(field_name='log_name', lookup_expr='icontains', label='log name')
    class Meta:
        model= LogBookSerial
        fields= '__all__'