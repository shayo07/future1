from django.shortcuts import render, redirect
from .filters import *
from .models import Madarasa
from Student.models import Mwanafunzi

from .models import GeneralResult
from .forms import *
from django.contrib.auth.decorators import login_required
from Student.decorators import *


import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
  
import csv

from django.http import HttpResponse
# Create your views here.




@allowed_user(allowed_roles='admin')
@login_required(login_url='login')
def add_somo(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = MasomoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subject')
    else:
        form = MasomoForm()
    context = {'form': form, 'a':a}
    return render(request, 'add_somo.html', context)



@login_required(login_url='login')
def view_masomo(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    
    if a:
     obj = Masomo.objects.all()
     myfilter = MasomoFilter(request.POST, queryset=obj)
     obj =myfilter.qs

     context = { 'obj':obj, 'a':a, 'myfilter':myfilter}
     return render(request, 'view_somo.html', context)
    else:
     obj = Masomo.objects.filter(teacher= request.user)
     myfilter = MasomoFilter(request.POST, queryset=obj)
     obj =myfilter.qs
     context = { 'obj':obj, 'a':a, 'myfilter':myfilter}
     return render(request, 'view_somo.html', context)
 


@allowed_user(allowed_roles='admin')
@login_required(login_url='login')   
def remove_somo(request, pk_test):
    obj = Masomo.objects.get(pk= pk_test)
    obj.delete()
    return redirect('view_subject')



@login_required(login_url='login')
def add_result(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Masomo.objects.get(pk=pk_test)
    if request.method == 'POST': 
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_subject')
    else:
        form = ResultForm(instance=obj)
    context = {'form': form, 'a':a}
    return render(request, 'add_result.html', context)


@login_required(login_url='login')
def view_result(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Result.objects.filter(subject_name = pk_test)
    t = Masomo.objects.get(subject_name=pk_test)
    myfilter= ResultFilter(request.POST, queryset=obj)
    obj= myfilter.qs
    context = {'obj':obj, 'a':a, 't':t, 'myfilter':myfilter}
    return render(request, 'result_list.html', context)
    



@login_required(login_url='login')
def edit_result(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj =Result.objects.get(id=pk_test)
    if request.method == 'POST': 
        form = ResultForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_subject')
    else:
        form = ResultForm(instance=obj)
    context = {'form': form, 'a':a}
    return render(request, 'add_result.html', context)



@login_required(login_url='login')   
def remove_result(request, pk_test):
    obj = Result.objects.get(id= pk_test)
    obj.delete()
    return redirect('view_subject')






@login_required(login_url='login')
def file_load_view(request, pk_test):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['darasa', 'student_id','subj1', 'total', 'average'])

    students = Result.objects.filter(subject_name = pk_test)

    # Note: we convert the students query set to a values_list as the writerow expects a list/tuple       
    students = students.values_list('darasa','student_id','subject_name', 'total', 'average')

    for student in students:
        writer.writerow(student)
    return response


 
from .models import GeneralResult
@login_required(login_url='login')
def import_csv(request):
    print('s')
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile= request.FILES['myfile']
            #fs = FileSystemStorage()
            #filename = myfile.save(myfile.name, myfile)
            print('here')
            empexceldata = pd.read_csv(myfile)
            print('i have pass')
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                obj = GeneralResult.objects.create(darasa=Madarasa.objects.get(class_id=dbframe.darasa),
                 student_id=Mwanafunzi.objects.get(student_id=dbframe.student_id), subj1=Masomo.objects.get(subject_name=dbframe.subj1), total= dbframe.total , average=dbframe.average )
                obj.save()
                print('done')
            return redirect('view_subjects')
    except Exception as identifier:
        print(identifier)
        print('i have pass here')
    return render(request, 'importexcel.html')





