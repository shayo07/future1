from django.db import models
from Student.models import Madarasa
from Subjects.models import Masomo
from django.contrib.auth.models import User
# Create your models here.





class SchoolJournal(models.Model):
    journal_name=models.CharField(max_length=200,primary_key=True, help_text='journal4a-t1-2021')
    class_id = models.ForeignKey(Madarasa, on_delete=models.SET_NULL, null=True, blank=True)
    class_teacher= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.journal_name


class RegisteredJournal(models.Model):
    journal_name= models.ForeignKey(SchoolJournal, on_delete=models.SET_NULL, null=True, blank=True)
    journal_id = models.CharField(max_length=40, primary_key=True, help_text='journ-4a-2022-07-12')
    date=models.DateField( null=True, blank=True)
    day= models.CharField(max_length=10, help_text='monday')
    def __str__(self):
        return self.journal_id



class RegisteredJournal1(models.Model):
    journal_name= models.ForeignKey(SchoolJournal, on_delete=models.SET_NULL, null=True, blank=True)
    journal_id = models.CharField(max_length=40, primary_key=True, help_text='journ-4a-2022-07-12')
    date=models.DateField( null=True, blank=True)
    day= models.CharField(max_length=10, help_text='monday')
    def __str__(self):
        return self.journal_id





class Journal(models.Model):
    time_select= (('session1','8:00-8:40'), ('session2','8:40-9:20'),  ('session3','9:20-10:0'), ('session4','10:00-10:40'),
                   ('session5','10:40-11:20'), ('session6','11:40-12:20'), ('session7','12:20-01:00'), ('session8','01:00-01:40'),
                   ('session9','01:40-02:20'), ('session10','03:00-04:00'))
    j_id = models.ForeignKey(RegisteredJournal1, on_delete=models.SET_NULL, null=True, blank=True)
    time=models.CharField(choices=time_select, max_length=20, blank=True, default='8:00-8:40') 
    period= models.CharField(max_length=2, help_text='1,2,3...', null=True, blank=True)
    subject_name= models.ForeignKey(Masomo, on_delete=models.SET_NULL, null=True, blank=True)
    concept_covered=models.CharField(max_length=200, null=True, blank=True)
    sub_teachers_comment= models.CharField(max_length=200, null=True, blank=True)
    sub_teachers_name= models.CharField(max_length=200, null=True, blank=True)
    class_leaders_comment= models.CharField(max_length=200, null=True, blank=True)
    class_teacher= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.time




class JournalDailyReport(models.Model):
    j_id = models.ForeignKey(RegisteredJournal1, on_delete=models.SET_NULL, null=True, blank=True)
    class_teacher= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    no_period_taught= models.CharField(max_length=200)
    number_periods_nottaught= models.CharField(max_length=200)
    reason_nottaught= models.CharField(max_length=200, null=True, blank=True)
    cl_comment= models.CharField(max_length=200, null=True, blank=True)
    ct_comment= models.CharField(max_length=200, null=True, blank=True)
    am_comment= models.CharField(max_length=200, null=True, blank=True)
    hs_comment= models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.no_period_taught
