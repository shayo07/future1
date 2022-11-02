from dataclasses import field, fields
from pyexpat import model
import django_filters
from .models import *
from Subjects.models import GeneralResult
from django_filters import CharFilter


class StudentFilter(django_filters.FilterSet):
    student_id= CharFilter(field_name='student_id', lookup_expr='icontains', label='student id')
    class Meta:
        model = Mwanafunzi
        fields = ['student_id', 'first_name', 'last_name']


class ClassFilter(django_filters.FilterSet):
    class_id = CharFilter(field_name='class_id', lookup_expr='icontains', label='class')
    class Meta:
        model= Madarasa
        fields = '__all__'

class ClassResultFilter(django_filters.FilterSet):
    class Meta:
        model= GeneralResult
        fields= ['student_id', 'subj1']