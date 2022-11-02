from django.db import models
from django.contrib.auth.models import User
from Subjects.models import Masomo
import uuid
# Create your models here.

class MainScheme(models.Model):
    scheme_name = models.CharField(primary_key=True, max_length=40, help_text='physics-4a-scheme-2020')
    subject_id =  models.ForeignKey(Masomo,on_delete=models.SET_NULL, null=True, blank=True )
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.scheme_name


class SchemeOfWork(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4, auto_created=True, primary_key=True, unique=True)
    serial_no = models.CharField(max_length=20, null=True, blank=True)
    scheme_name= models.ForeignKey(MainScheme, on_delete=models.SET_NULL, null=True, blank=True)
    competence= models.TextField( null=True, blank=True)
    objectives= models.TextField( null=True, blank=True)
    month= models.CharField(max_length=20,  null=True, blank=True)
    week= models.CharField(max_length=2, help_text='namba ya wiki',  null=True, blank=True)
    main_topic= models.CharField(max_length=200,  null=True, blank=True)
    sub_topic= models.TextField( null=True, blank=True)
    periods= models.CharField(max_length=2,  null=True, blank=True)
    teaching_activities= models.TextField( null=True, blank=True) 
    learning_activities= models.TextField( null=True, blank=True)
    references= models.TextField( null=True, blank=True)
    teaching_aids= models.TextField( null=True, blank=True)
    assesments= models.TextField( null=True, blank=True)
    remarks= models.TextField( null=True, blank=True)
    
    def __str__(self):
        return f'{self.scheme_name, self.competence}'