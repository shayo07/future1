
from django.shortcuts import render
from .filters import *
from .forms import SAttendanceForm
from Student.decorators import *
from .models import *
from django.forms import inlineformset_factory
from Student.models import Darasa, Madarasa
from django.contrib.auth.decorators import login_required
# Create your views here.



@admin_only
@login_required
def add_sattendance(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = SAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sattendance')
    else:
        form = SAttendanceForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_satt.html', context)


@login_required(login_url='login')
def view_sattendance(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = SchoolAttendance.objects.all()
        myfilter=SaFilter(request.POST, queryset=obj)
        obj=myfilter.qs
    else:
        obj = SchoolAttendance.objects.filter(username = request.user)
        myfilter=SaFilter(request.POST, queryset=obj)
        obj=myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_satt.html', context)


@login_required
def remove_sattendance(request, pk_test):
    obj = SchoolAttendance.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sattendance')




@login_required
def add_attendance(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()  
    obj1 = SchoolAttendance.objects.get(pk = pk_test)
    obj01= Madarasa.objects.get(teacher=request.user)
    wana= obj01.darasa_set.all()
    if request.method == 'POST':
         a = dict(request.POST)
         b=a.POST('obj1')
         c=a.POST('obj2')
         d=a.POST('status')
         for x,y,z in zip(b,c,d):
                
                 Attendance.objects.create(attendance_name=SchoolAttendance.objects.get(attendance_name=x),
                 student_id=Mwanafunzi.objects.get(student_id=y), status=z)
                 
         return HttpResponse('sent successful')
    context = {'wana':wana, 'a':a,  'obj1':obj1}
    return render(request, 'add_att.html', context)


@login_required
def view_attendance(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Attendance.objects.filter(attendance_name=pk_test)
    myfilter=AttFilter(request.POST, queryset=obj)
    obj=myfilter.qs
    context = {'obj':obj, 'a':a, 'pk_test':pk_test, 'myfilter':myfilter}
    return render(request, 'view_att.html', context)


@login_required
def remove_attendance(request, pk_test):
    obj = Attendance.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sattendance')