from dataclasses import fields
from pyexpat import model
import django_filters
from .models import SchoolAttendance, Attendance
from django_filters import CharFilter

class SaFilter(django_filters.FilterSet):
    attendance_name= CharFilter(field_name='attendance_name', lookup_expr='icontains', label='attendance name')
    class Meta:
        model= SchoolAttendance
        fields= '__all__'

class AttFilter(django_filters.FilterSet):
    date= CharFilter(field_name='date', lookup_expr='icontains', label='date')
    class Meta:
        model= Attendance
        fields= '__all__'
        exclude= 'attendance_name'
        