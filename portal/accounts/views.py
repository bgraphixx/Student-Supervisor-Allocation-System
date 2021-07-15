from django.http.response import HttpResponse
from django.shortcuts import render, redirect
#import django default form for user creation
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    context = {}
    return render(request, 'accounts/index.html', context)
    
def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('user_type')
    else:
        form = CreateUserForm() #create usercreation for

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
    
@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def usertype(request):
    myuser = request.user
    if request.method == 'POST':
        pform = ProfileForm(request.POST)
        if pform.is_valid():
            profile = pform.save(commit=False)
            if profile.user_type == 'Student':
                group = Group.objects.get(name='Students')
                myuser.groups.add(group)
                messages.success(request,'Profile Completed')
                profile.user = myuser
                profile.save()
                return redirect('student_info')
            elif profile.user_type == 'Supervisor':
                group = Group.objects.get(name='Supervisors')
                messages.success(request,'Profile Completed')
                profile.user = myuser
                profile.save()
                return redirect('supervisor_info')
        else:
            messages.error(request, 'Invalid input')                  
    else:
            pform = ProfileForm()

    context = {
        'pform': pform
    }
    return render(request, 'accounts/usertype.html', context)

@login_required
def student_info(request):
    myuser = request.user
    if request.method == 'POST':
        stinfoform = StudentForm(request.POST)
        if stinfoform.is_valid():
            stinfo = stinfoform.save(commit=False)
            stinfo.student = myuser
            messages.success(request,'Successfully saved student information!')
            stinfo.save()
            return redirect('student_dashboard')
    else:
            stinfoform = StudentForm()

    context = {
        'stinfoform': stinfoform
    }
    return render(request, 'accounts/studentinfo.html', context)

@login_required
def supervisor_info(request):
    myuser = request.user
    if request.method == 'POST':
        supinfoform = SupervisorForm(request.POST)
        if supinfoform.is_valid():
            supinfo = supinfoform.save(commit=False)
            supinfo.staff = myuser
            messages.success(request,'Successfully saved supervisor information!')
            supinfo.save()
            return redirect('super_dashboard')
    else:
            supinfoform = SupervisorForm()

    context = {
        'supinfoform': supinfoform
    }
    return render(request, 'accounts/supervisorinfo.html', context)

@login_required
def dashboard(request):
    myuser = request.user
    if myuser.groups.filter(name='Students'):
        return redirect('student_dashboard')
    else:
        return redirect('super_dashboard')

@login_required
def super_dashboard(request):
    myuser = request.user
    superlevel = Supervisors.objects.get(staff=myuser).staff_level
    superdepartment = Supervisors.objects.get(staff=myuser).department
    context = {
        'superlevel': superlevel,
        'superdepartment': superdepartment,
    }
    return render(request, 'accounts/supervisordashboard.html', context)


@login_required
def student_dashboard(request):
    myuser = request.user
    stlevel = Students.objects.get(student=myuser).level
    stdepartment = Students.objects.get(student=myuser).department
    stcourse = Students.objects.get(student=myuser).course
    areadb = AreaOfInterests.objects.filter(user=myuser).exists()
    context = {
        'areadb' : areadb,
        'stlevel': stlevel,
        'stdepartment': stdepartment,
        'stcourse' : stcourse
    }
    return render(request, 'accounts/studentdashboard.html', context)

@login_required
def rankarea(request):
    myuser = request.user
    if request.method == 'POST':
        areaform = AreaOfInterestsForm(request.POST)
        if areaform.is_valid():
            arearank = areaform.save(commit=False)
            arearank.user = myuser
            messages.success(request, f'Area of Interest saved!')
            arearank.save()
            if myuser.groups.filter(name='Students'):
                return redirect('student_dashboard')
            else:
                return redirect('super_dashboard')
    else:
        areaform = AreaOfInterestsForm()
    context = {
        'areaform': areaform,
    }
    return render(request, 'accounts/rank_area.html', context)

@login_required
def updaterankarea(request, id):
    myuser = request.user
    myarearank = AreaOfInterests.objects.get(user=myuser)
    areaform = AreaOfInterestsForm(instance=myarearank)
    if request.method == 'POST':
        areaform = AreaOfInterestsForm(request.POST, instance=myarearank)
        if areaform.is_valid():
            messages.success(request, f'Area of Interest has been updated!')
            areaform.save()
            return redirect('student_dashboard')
    context = {
        'areaform': areaform
    }
    return render(request, 'accounts/rank_area.html', context)