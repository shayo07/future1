from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Mwanafunzi(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_name= models.CharField(max_length=40)
    dob = models.DateField(default='2022-12-12')
    dob = models.DateField(default=2022-12-12)
    address = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=13)
    year_administered = models.CharField(max_length=4, default='2049')
    student_id = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.student_id
    
 
 

class Madarasa(models.Model):
    class_id = models.CharField(max_length=60, primary_key=True, help_text='form-1a-2020')
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.class_id

class Darasa(models.Model):
    student_id = models.ForeignKey(Mwanafunzi, on_delete=models.SET_NULL, null=True, blank=True)
    class_id = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.student_id}'

class Teacher_Info(models.Model):
    username= models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50, null=True, blank=True)
    middle_name=models.CharField(max_length=50, null=True, blank=True)
    last_name=models.CharField(max_length=50, null=True, blank=True)
    tin_number=models.CharField(max_length=50, null=True, blank=True)
    email=models.CharField(max_length=50, null=True, blank=True)
    profile_pic=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email
