from django.db import models
from django.contrib.auth.models import User
from Student.models import  Madarasa, Mwanafunzi
# Create your models here.

STAGE_CHOICE=(('present', 'present'),
                  ('absent', 'absent'),
                  ('sick', 'sick')
              
                )

class SchoolAttendance(models.Model):
    attendance_name = models.CharField(max_length=100, primary_key=True, help_text='form-4a-2022-att')
    class_name = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.attendance_name

class Attendance(models.Model):
    attendance_name= models.ForeignKey(SchoolAttendance, on_delete=models.SET_NULL, null=True, blank=True)
    student_id=models.ForeignKey(Mwanafunzi, on_delete=models.SET_NULL, null=True, blank=True)
    status= models.CharField(max_length=30, default='absent', choices=STAGE_CHOICE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.attendance_name},{self.date}'