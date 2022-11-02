from celery import uuid
from django.db import models
from Subjects.models import Masomo
from django.contrib.auth.models import User
import uuid
# Create your models here.



class LogBookSerial(models.Model):
    log_name= models.CharField(max_length=100, primary_key=True, help_text='physics-4a-log-2020')
    subject_id=models.ForeignKey(Masomo, on_delete=models.SET_NULL, null=True, blank=True)
    username= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self):
        return self.log_name


class Logbook(models.Model):
    id = models.CharField(max_length=40, default=uuid.uuid4, auto_created=True, primary_key=True, unique=True)
    sno= models.CharField(max_length=4, default='01')
    log_name= models.ForeignKey(LogBookSerial, on_delete=models.SET_NULL, null=True, blank=True)
    week_no= models.CharField(max_length=2, null=True, blank=True)
    month_no= models.CharField(max_length=2, null=True, blank=True)
    main_topic= models.TextField(max_length=200, null=True, blank=True)
    sub_topic=models.TextField(max_length=200, null=True, blank=True)
    time_start= models.DateField(null=True, blank=True)
    time_finish= models.DateField(null=True, blank=True)
    concept_covered= models.TextField( null=True, blank=True)
    teachers_comment  = models.CharField(max_length=40, null=True, blank=True)
    hod = models.CharField(max_length=40, blank=True, null=True)
    head_teacher= models.CharField(max_length= 40, null=True, blank=True)
    

    def __str__ (self):
        return self.sno