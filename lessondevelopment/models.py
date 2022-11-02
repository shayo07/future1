from django.db import models
from django.contrib.auth.models import User
from Subjects.models import Masomo
from Student.models import Madarasa
# Create your models here.


class SchoolTplan(models.Model):
    id = models.CharField(max_length=40, primary_key=True, help_text='kiswa-lp-t1-2022')
    subject= models.ForeignKey(Masomo, on_delete=models.SET_NULL, null=True, blank=True)
    username= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.id


class Tplan(models.Model):
     school_id = models.ForeignKey(SchoolTplan, on_delete=models.SET_NULL, null=True, blank=True)
     lesson_id= models.CharField(primary_key=True,max_length=30, help_text='lesson01-term1-2021')
     class_id= models.ForeignKey(Madarasa, on_delete=models.SET_NULL, null=True, blank=True)
     

     def __str__(self):
         return self.lesson_id


class LessonPlan(models.Model):
    lesson_id= models.ForeignKey(Tplan, on_delete=models.SET_NULL, null=True, blank=True)
    period= models.CharField(max_length=10, help_text='number of period', null=True, blank=True)
    time= models.CharField(max_length=10, help_text='example 4hrs', null=True, blank=True)
    boy_registered=models.CharField(max_length=10, null=True, blank=True)
    girls_registered=models.CharField(max_length=10, null=True, blank=True)
    boy_present=models.CharField(max_length=10, null=True, blank=True)
    girls_present=models.CharField(max_length=10, null=True, blank=True)
    competence= models.CharField(max_length=400, null=True, blank=True)
    topic= models.CharField(max_length=400, null=True, blank=True)
    sub_topic= models.TextField(max_length=400, null=True, blank=True)
    general_objectives= models.TextField(max_length=700, null=True, blank=True)
    specific_objectives= models.TextField(max_length=1000, null=True, blank=True)
    T_learning_materials=models.TextField(max_length=1000, null=True, blank=True)
    reference= models.TextField(max_length=500, null=True, blank=True)


    def __str__(self):
        return self.topic

class Lesson_development(models.Model):
    STAGE_CHOICE=(('introduction', 'introduction'),
                  ('developing new knowledge', 'developing new knowledge'),
                  ('reinforcement', 'reinforcement'),
                  ('reflection', 'reflection'),
                  ('consolidation', 'consolidation'),
                )
    lesson_id= models.ForeignKey(Tplan, on_delete=models.SET_NULL, null=True, blank=True)
    stage= models.CharField(max_length=30, default='introduction', choices=STAGE_CHOICE, null=True, blank=True)
    time= models.CharField(max_length=10, help_text='example 4hrs', null=True, blank=True)
    teaching_activities=models.TextField(null=True, blank=True)
    learning_activities=models.TextField( null=True, blank=True)
    assesment= models.TextField( null=True, blank=True)
  

    def __str__ (self):
        return self.stage

class LessonEvaluation(models.Model):
    lesson_id= models.ForeignKey(Tplan, on_delete=models.SET_NULL, null=True, blank=True)
    student_eval= models.TextField( null=True, blank=True)
    teacher_eval= models.TextField( null=True, blank=True)
    remarks= models.TextField( null=True, blank=True)

    def __str__(self):
        return f'{self.lesson_id}, {self.remarks}'
