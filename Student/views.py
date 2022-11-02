
from multiprocessing import context
from django.shortcuts import redirect, render
from .filters import *

from Subjects.models import Masomo, GeneralResult
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *

from django.contrib.auth.models import Group

# Create your views here.

def index(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    c= request.user
    d=c.teacher_info_set.all()
    context = {'a': a, 'd':d}
    return render(request, 'home.html', context)




@unauthenticated_user
def log_user(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'incorrect username or password')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')

@allowed_user(allowed_roles='admin')
def register_user(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name = 'teacher')
            user.groups.add(group)

            messages.success(request, 'you have been registered successful for'+ username)
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {'form':form, 'a': a}
    return render(request, 'registration.html', context)



@login_required(login_url='login')
def teachers(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
   
    obj = User.objects.all()    
    obj1= Teacher_Info.objects.filter(username=request.user)
    context= {'obj':obj, 'a':a, 'obj1':obj1}
    return render(request, 'view_teacher.html', context)


@login_required(login_url='login')
def edit_teacher(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Teacher_Info.objects.get(id=pk_test)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=obj )
        if form.is_valid():
            form.save()
            return redirect('teachers') 
    else:
        form = TeacherForm(instance=obj)
    context = {'form': form, 'a': a}
    return render(request, 'add_tinfo.html', context)


@login_required(login_url='login')
def add_teacher(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect('teachers') 
    else:
        form = TeacherForm()
    context = {'form': form, 'a': a}
    return render(request, 'add_tinfo.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def remove_teacher(request, pk_test):
    cl = User.objects.get(pk=pk_test)
    cl.delete()
    return  redirect('view_student')


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def add_student(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student') 
    else:
        form = StudentForm()
    context = {'form': form, 'a': a}
    return render(request, 'add_student.html', context)


@login_required(login_url='login')
@admin_only
def view_students(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    data = Mwanafunzi.objects.all()
    myfilter = StudentFilter(request.POST, queryset=data)
    data = myfilter.qs
    context = {'data': data, 'a': a, 'myfilter':myfilter}
    return render(request, 'student_list.html', context)


@login_required(login_url='login')
def student_details(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Mwanafunzi.objects.get(student_id=pk_test)
    context = {'obj':obj, 'a':a}
    return render(request, 'student_detail.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def edit_student(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj= Mwanafunzi.objects.get(pk=pk_test)
    if request.method== 'POST':
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    else:
        form = StudentForm(instance=obj)
    context = {'form':form, 'a': a}
    return render(request, 'add_student.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def remove_student(request, pk_test):
    cl = Mwanafunzi.objects.get(pk=pk_test)
    cl.delete()
    return  redirect('view_student')


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def add_classes(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = MadarasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_classes')
    else:
        form = MadarasaForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_madarasa.html', context)




@login_required(login_url='login')
def view_classes(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = Madarasa.objects.all()
        myfilter = ClassFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    else:
        obj = Madarasa.objects.filter(teacher=request.user)
        myfilter = ClassFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_madarasa.html', context)


@login_required(login_url='login')
def class_details(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    data = Madarasa.objects.get(pk=pk_test)
    wanafunzi= data.darasa_set.all()
    context = {'data':data, 'wanafunzi':wanafunzi, 'a':a}
    return render(request, 'class_details.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def remove_class(request, pk_test):
    cl = Madarasa.objects.get(pk=pk_test)
    cl.delete()
    return  redirect('view_classes')







@login_required(login_url='login')
def add_darasa(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Madarasa.objects.get(pk=pk_test)
    if request.method== 'POST':
        
        form = DarasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_classes')
    else:
        form = DarasaForm(instance=obj)
    context = {'form':form,  'a':a}
    return render(request, 'add_darasa.html', context)



@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def view_cstudent(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    cl= Darasa.objects.filter(class_id=pk_test)
 
    context = {'cl':cl, 'a':a}
    return  render(request, 'class_student.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def remove_cstudent(request, pk_test):
    cl = Darasa.objects.get(id=pk_test)
    cl.delete()
    return  redirect('view_classes')


@login_required
def general_class_result(request, pk_test):
    data = Madarasa.objects.get(pk=pk_test)
    data2 = data.generalresult_set.all().order_by("student_id_id")
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    myfilter= ClassResultFilter(request.POST, queryset=data2)
    data2= myfilter.qs
    context = {'data':data2, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_stu.html', context) 

@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def remove_gresult(request, pk_test):
    cl = GeneralResult.objects.get(id=pk_test)
    cl.delete()
    return  redirect('view_classes')


@login_required
def student_result(request, pk_test):
    data1 = Mwanafunzi.objects.get(pk=pk_test)
    data2 = data1.result_set.all()
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()


    context = {'data':data2, 'a':a}
    return render(request, 'student_result.html', context)