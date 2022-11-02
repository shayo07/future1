from dataclasses import fields
import django_filters
from .models import SchoolJournal, RegisteredJournal
from django_filters import CharFilter


class SjFilter(django_filters.FilterSet):
    journal_name=CharFilter(field_name='journal_name', lookup_expr='icontains', label='journal name')
    class Meta:
        model = SchoolJournal
        fields= '__all__'

class RjFilter(django_filters.FilterSet):
    journal_id=CharFilter(field_name='journal_id', lookup_expr='icontains', label='journal')
    day=CharFilter(field_name='day', lookup_expr='icontains', label='day')
    date=CharFilter(field_name='date', lookup_expr='icontains', label='date')
    class Meta:
        model=RegisteredJournal
        fields = '__all__'
        exclude= 'journal_name'