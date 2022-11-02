from django.shortcuts import render, redirect

from .filters import *
from .models import *
from Student.decorators import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@admin_only
@login_required
def add_stplan(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = SchoolTplanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = SchoolTplanForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_stplan.html', context)


@login_required(login_url='login')
def view_stplan(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if a:
        obj = SchoolTplan.objects.all()
        myfilter= StplanFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    else:
        obj = SchoolTplan.objects.filter(username = request.user)
        myfilter= StplanFilter(request.POST, queryset=obj)
        obj = myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_stplan.html', context)


@login_required
def remove_stplan(request, pk_test):
    obj = SchoolTplan.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_stplan')







@login_required
def add_tplan(request):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    if request.method == 'POST':
        form = TplanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = TplanForm()
    context = {'form':form, 'a':a}
    return render(request, 'add_tplan.html', context)


@login_required
def view_tplan(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj1 = SchoolTplan.objects.get(pk=pk_test)
    obj = obj1.tplan_set.all()
    myfilter= TplanFilter(request.POST, queryset=obj)
    obj=myfilter.qs
    context = {'obj':obj, 'a':a, 'myfilter':myfilter}
    return render(request, 'view_tplan.html', context)



@login_required
def edit_tplan(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Tplan.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = TplanForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = TplanForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_tplan.html', context)


@login_required
def remove_tplan(request, pk_test):
    obj = Tplan.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_stplan')








@login_required
def add_lessonplan(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Tplan.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessonplanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = LessonplanForm(instance=obj)
    context = {'form':form, 'a':a, 'pk_test':pk_test}
    return render(request, 'add_lplan.html', context)

@login_required
def edit_lessonplan(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = LessonPlan.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessonplanForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form =LessonplanForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_lplan.html', context)

@login_required
def remove_lessonplan(request, pk_test):
    obj = LessonPlan.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_stplan')






@login_required
def add_lessondev(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Tplan.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessondevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = LessondevForm(instance=obj)
    context = {'form':form, 'a':a, 'pk_test':pk_test}
    return render(request, 'add_ldev.html', context)


@login_required
def edit_lessondev(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Lesson_development.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessondevForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form =LessondevForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_ldev.html', context)

@login_required
def remove_lessondev(request, pk_test):
    obj = Lesson_development.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_stplan')



@login_required
def add_lessoneval(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = Tplan.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessonevalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form = LessonevalForm(instance=obj)
    context = {'form':form, 'a':a, 'pk_test':pk_test}
    return render(request, 'add_leval.html', context)


@login_required
def edit_lessoneval(request, pk_test):
    def choose():
        if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group == 'admin':
                 return group
    a=choose()
    obj = LessonEvaluation.objects.get(pk=pk_test)
    if request.method == 'POST':
        form = LessonevalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('view_stplan')
    else:
        form =LessonevalForm(instance=obj)
    context = {'form':form, 'a':a}
    return render(request, 'add_leval.html', context)


@login_required
def remove_lessoneval(request, pk_test):
    obj = LessonEvaluation.objects.get(pk=pk_test)
    obj.delete()
    return redirect('view_stplan')



def view_lessonplan(request, pk_test):
    obj1 = Tplan.objects.get(lesson_id=pk_test) 
    obj2=obj1.lessonplan_set.all()
    obj3=obj1.lesson_development_set.all()
    obj4 = obj1.lessonevaluation_set.all()
    context={'obj1':obj1,'obj2':obj2,'obj3':obj3,'obj4':obj4}
    return render(request, 'view_lessonplan.html', context)


