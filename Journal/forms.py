from django import forms
from .models import *

class SchoolJournalForm(forms.ModelForm):
    class Meta:
        model = SchoolJournal
        fields = '__all__'


class RJournalForm(forms.ModelForm):
    class Meta:
        model = RegisteredJournal1
        fields= '__all__'


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields= '__all__'


class JournalDrForm(forms.ModelForm):
    class Meta:
        model = JournalDailyReport
        fields= '__all__'

