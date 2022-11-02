from django import forms
from .models import *



class SAttendanceForm(forms.ModelForm):
    class Meta:
        model = SchoolAttendance
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
