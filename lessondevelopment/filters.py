import django_filters
from .models import SchoolTplan, Tplan
from django_filters import CharFilter


class StplanFilter(django_filters.FilterSet):
    id = CharFilter(field_name='id', lookup_expr='icontains' ,label='main lessonplan')
    class Meta:
        model=SchoolTplan
        fields='__all__'


class TplanFilter(django_filters.FilterSet):
    lesson_id = CharFilter(field_name='lesson_id', lookup_expr='icontains', label='lesson name')
    class Meta:
        model = Tplan
        fields = '__all__'
        exclude='school_id'
