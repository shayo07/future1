from dataclasses import fields
import django_filters
from .models import MainScheme
from django_filters import CharFilter



class MschemeFilter(django_filters.FilterSet):
    scheme_name= CharFilter(field_name='scheme_name', lookup_expr='icontains', label='scheme name')
    class Meta:
        model=MainScheme
        fields = '__all__'
        