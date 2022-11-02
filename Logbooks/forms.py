from django import forms
from . models import *

class LogbookserialForm(forms.ModelForm):
    class Meta:
        model = LogBookSerial
        fields = '__all__'


class LogbookForm(forms.ModelForm):
    class Meta:
        model = Logbook
        fields = ['sno', 'log_name', 'week_no', 'week_no', 'month_no', 'main_topic',
        'sub_topic', 'time_start', 'time_finish', 'concept_covered', 'teachers_comment', 'hod', 'head_teacher']