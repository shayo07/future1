import django_filters
from .models import *
from django_filters import CharFilter

class MasomoFilter(django_filters.FilterSet):
    subject_name= CharFilter(field_name='subject_name', lookup_expr='icontains', label='subject name')
    class Meta:
        model = Masomo
        fields = '__all__'


class ResultFilter(django_filters.FilterSet):
    class Meta:
        model = Result
        fields= ['darasa', 'subject_name', 'student_id']