from django import forms
from .models import *


class MainschemeForm(forms.ModelForm):
    class Meta:
        model = MainScheme
        fields = '__all__'


class SchemeofworkForm(forms.ModelForm):
    class Meta:
        model = SchemeOfWork
        fields = '__all__'