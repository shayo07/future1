from django.shortcuts import render, redirect
from .models import *
from Student.decorators import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@admin_only
@login_required(login_url='login')
def add_sjourn(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = SchoolJournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form = SchoolJournalForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_sjourn.html', context)


@login_required(login_url='login')
def view_sjourn(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = SchoolJournal.objects.all()
        myfilter = SjFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    else:
        obj = SchoolJournal.objects.filter(class_teacher = request.user)
        myfilter = SjFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_sjourn.html', context)


@login_required(login_url='login')
def remove_sjourn(request, pk_test):
    obj = SchoolJournal.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sjourn')







@login_required(login_url='login')
def add_rjourn(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = RJournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form = RJournalForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_rjourn.html', context)


@login_required(login_url='login')
def view_rjourn(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj1= SchoolJournal.objects.get(pk=pk_test)
    obj = obj1.registeredjournal1_set.all()
    myfilter=RjFilter(request.POST, queryset=obj)
    obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_rjourn.html', context)



@login_required(login_url='login')
def edit_rjourn(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = RegisteredJournal1.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = RJournalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form = RJournalForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_rjourn.html', context)


@login_required(login_url='login')
def remove_rjourn(request, pk_test):
    obj= RegisteredJournal1.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sjourn')








@login_required(login_url='login')
def add_journal(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
  
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form = JournalForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_journ.html', context)

@login_required(login_url='login')
def edit_journ(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Journal.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form =JournalForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_journ.html', context)

@login_required(login_url='login')
def remove_journ(request, pk_test):
    obj = Journal.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sjourn')






@login_required(login_url='login')
def add_journdr(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj= RegisteredJournal1.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = JournalDrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form = JournalDrForm(instance=obj)
    context = {'form':form, 'a':a, 'pk_test':pk_test}
    return render(request, 'add_jdr.html', context)


@login_required(login_url='login')
def edit_journdr(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj =RegisteredJournal1.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = JournalDrForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_sjourn')
    else:
        form =JournalDrForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_jdr.html', context)

@login_required(login_url='login')
def remove_journdr(request, pk_test):
    obj = JournalDailyReport.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_sjourn')





def view_myjournal(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj1= RegisteredJournal1.objects.get(pk=pk_test) 
    obj2=obj1.journal_set.all()
    obj3=obj1.journaldailyreport_set.all()
    context={'obj1':obj1,'obj2':obj2,'obj3':obj3, 'a':a}
    return render(request, 'view_myjourn.html', context)


