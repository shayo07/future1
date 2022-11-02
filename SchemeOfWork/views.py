from .filters import *
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from Student.decorators import admin_only
# Create your views here.
@admin_only
@login_required(login_url='login')
def add_mainscheme(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = MainschemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_main_scheme')
    else:
        form = MainschemeForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_mainscheme.html', context)


@login_required(login_url='login')
def view_mscheme(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = MainScheme.objects.all()
        myfilter= MschemeFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    else:
        obj = MainScheme.objects.filter(teacher = request.user)
        myfilter= MschemeFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_mainscheme.html', context)

    
@admin_only
@login_required(login_url='login')
def remove_mscheme(request, pk_test):
    obj = MainScheme.objects.get(scheme_name=pk_test)
    obj.delete()
    return redirect('view_main_scheme')





@login_required(login_url='login')
def add_scheme(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = MainScheme.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = SchemeofworkForm(request.POST)
        if form.is_valid():
            take = form.cleaned_data['scheme_name']
            p = MainScheme.objects.filter(teacher=request.user)
            for x in p:
                if x == take:
                    form.save()
                    return redirect('view_main_scheme')
    else:
        form = SchemeofworkForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_scheme.html', context)


@login_required(login_url='login')
def view_scheme(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = SchemeOfWork.objects.filter(scheme_name=pk_test)
    context = {'obj':obj, 'a':a, 'pk_test':pk_test}
    return render(request, 'view_scheme.html', context)

@login_required(login_url='login')
def edit_scheme(request, id):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        obj = SchemeOfWork.objects.get(id=id)
        form = SchemeofworkForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_main_scheme')
    else:
        obj = SchemeOfWork.objects.get(id=id)
        form = SchemeofworkForm(instance= obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_scheme.html', context)


@login_required(login_url='login')
def remove_scheme(request, id):
    obj = SchemeOfWork.objects.get(id=id)
    obj.delete()
    return redirect('view_main_scheme' )