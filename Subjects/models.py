
from django.db import models
from Student.models import Madarasa, Mwanafunzi
from django.contrib.auth.models import User
# Create your models here.


class Masomo(models.Model):
    subject_name = models.CharField(max_length=20, primary_key=True, help_text='kiswahili-4a-2022')
    class_id = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.subject_name




GRADE_CHOICE=(('A', 'A'),
                  ('B', 'B'),
                  ('C', 'C'),
                  ('D', 'D'),
                  ('F', 'F'),
                )

class Result(models.Model):
    darasa = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, blank=True, null=True)
    subject_name = models.ForeignKey(Masomo, on_delete=models.SET_NULL, null=True, blank=True)
    student_id = models.ForeignKey(Mwanafunzi, on_delete=models.SET_NULL, null=True, blank=True)
    test1= models.CharField(max_length=5, null=True, blank=True, default=0)
    test2= models.CharField(max_length=5, null=True, blank=True, default=0)
    test3= models.CharField(max_length=5, null=True, blank=True, default=0)
    mid= models.CharField(max_length=5, null=True, blank=True, default=0)
    test4= models.CharField(max_length=5, null=True, blank=True, default=0)
    test5= models.CharField(max_length=5, null=True, blank=True, default=0)
    total_test= models.CharField(max_length=5, null=True, blank=True, default=0)
    test_average= models.CharField(max_length=5,null=True, blank=True, default=0)
    term1_exam= models.CharField(max_length=5,null=True, blank=True, default=0)
    total= models.CharField(max_length=5,null=True, blank=True, default=0)
    average= models.CharField(max_length=5,null=True, blank=True, default=0)
    grades= models.CharField(max_length=5,null=True, blank=True, choices=GRADE_CHOICE)
    remarks=models.CharField(max_length=5,null=True, blank=True)

    def __str__(self):
        return f'{self.subject_name, self.student_id, self.total}'

class GeneralResult(models.Model):
    darasa = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, blank=True, null=True)
    student_id = models.ForeignKey(Mwanafunzi, on_delete=models.SET_NULL, null=True, blank=True)
    subj1= models.ForeignKey(Masomo, on_delete=models.SET_NULL, blank=True, null=True)
    total= models.CharField(max_length=4, null=True, blank=True)
    average= models.CharField(max_length=4, null=True, blank=True)


    def __str__(self):
        return f'{self.subj1, self.student_id, self.total}'