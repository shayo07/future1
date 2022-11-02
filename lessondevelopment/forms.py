from django import forms
from .models import *

class SchoolTplanForm(forms.ModelForm):
    class Meta:
        model = SchoolTplan
        fields = '__all__'


class TplanForm(forms.ModelForm):
    class Meta:
        model = Tplan
        fields= '__all__'


class LessonplanForm(forms.ModelForm):
    class Meta:
        model = LessonPlan
        fields= '__all__'


class LessondevForm(forms.ModelForm):
    class Meta:
        model = Lesson_development
        fields= '__all__'

class LessonevalForm(forms.ModelForm):
    class Meta:
        model = LessonEvaluation
        fields= '__all__'