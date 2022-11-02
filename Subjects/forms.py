from django import forms
from .models import Masomo, Result

class MasomoForm(forms.ModelForm):
    class Meta:
        model = Masomo
        fields = '__all__'


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'