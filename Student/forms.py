from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model = Mwanafunzi
        fields = '__all__'


class MadarasaForm(forms.ModelForm):
    class Meta:
        model = Madarasa
        fields = '__all__'

class DarasaForm(forms.ModelForm):
    class Meta:
        model = Darasa
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher_Info
        fields = '__all__'