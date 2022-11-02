from .filters import *
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from Student.decorators import admin_only
# Create your views here.

@admin_only
@login_required(login_url='login')
def add_logbookserial(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = LogbookserialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_logbook_serial')
    else:
        form = LogbookserialForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_mlogbook.html', context)


@login_required(login_url='login')
def view_logbookserial(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = LogBookSerial.objects.all()
        myfilter =LogBookSFilter(request.GET, queryset=obj)
        obj = myfilter.qs
    else:
        obj = LogBookSerial.objects.filter(username = request.user)
        myfilter =LogBookSFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_mainlogbook.html', context)

    
@admin_only
@login_required(login_url='login')
def remove_logbookserial(request, pk_test):
    obj = LogBookSerial.objects.get(log_name=pk_test)
    obj.delete()
    return redirect('view_logbook_serial')



@login_required(login_url='login')
def add_logbook(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = LogBookSerial.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LogbookForm(request.POST)
        if form.is_valid():
          take = form.cleaned_data['log_name']
          q=LogBookSerial.objects.filter(username=request.user)
          for p in q:
            if p == take:
                form.save()
                return redirect('view_logbook_serial')
    else:
        form = LogbookForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_logbook.html', context)


@login_required(login_url='login')
def view_logbook(request, pk_test):
    data = LogBookSerial.objects.get(pk=pk_test)
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Logbook.objects.filter(log_name=pk_test)
    context = {'obj':obj, 'pk_test':pk_test, 'a':a}
    return render(request, 'view_logbook.html', context)

@login_required(login_url='login')
def edit_logbook(request, id):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        obj = Logbook.objects.get(id=id)
        form = LogbookForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_logbook_serial')
    else:
        obj = Logbook.objects.get(id=id)
        form = LogbookForm(instance= obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_logbook.html', context)


@login_required(login_url='login')
def remove_logbook(request, id):
    obj = Logbook.objects.get(id=id)
    obj.delete()
    return redirect('view_logbook_serial' )