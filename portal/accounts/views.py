from django.http.response import HttpResponse
from django.shortcuts import render, redirect
#import django default form for user creation
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
    
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
            elif profile.user_type == 'Admin':
                group = Group.objects.get(name='Administrators')
                messages.success(request, 'Profile Completed')
                profile.user = myuser
                profile.save()
                return redirect('admin_info')
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
def administrator_info(request):
    myuser = request.user
    if request.method == 'POST':
        adinfoform = AdministratorForm(request.POST)
        if adinfoform.is_valid():
            adinfo = adinfoform.save(commit=False)
            adinfo.staff = myuser
            messages.success(request,'Successfully saved Administrator information!')
            adinfo.save()
            return redirect('admin_dashboard')
    else:
            adinfoform = AdministratorForm()

    context = {
        'adinfoform': adinfoform
    }
    return render(request, 'accounts/adminsinfo.html', context)

@login_required
def dashboard(request):
    myuser = request.user
    if myuser.groups.filter(name='Students'):
        return redirect('student_dashboard')
    elif myuser.groups.filter(name='Supervisors'):
        return redirect('super_dashboard')
    else:
        return redirect('admin_dashboard')

@login_required
def super_dashboard(request):
    myuser = request.user
    mysupervisor = Supervisors.objects.get(staff=myuser)
    superlevel = mysupervisor.staff_level
    superdepartment = mysupervisor.department
    areadb = SupervisorsAreaOfInterests.objects.filter(supervisor=mysupervisor).exists()
    context = {
        'areadb': areadb,
        'superlevel': superlevel,
        'superdepartment': superdepartment,
    }
    return render(request, 'accounts/supervisordashboard.html', context)


@login_required
def student_dashboard(request):
    myuser = request.user
    mystudent = Students.objects.get(student=myuser)
    stlevel = mystudent.level
    stdepartment = mystudent.department
    stcourse = mystudent.course
    areadb = StudentsAreaOfInterests.objects.filter(student=mystudent).exists()
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
    if myuser.groups.filter(name='Students'):
        mystudent = Students.objects.get(student=myuser)
        print(mystudent)
        if request.method == 'POST':
            areaform = StudentsAreaOfInterestsForm(request.POST)
            if areaform.is_valid():
                arearank = areaform.save(commit=False)
                arearank.student = mystudent
                messages.success(request, f'Area of Interest saved!')
                arearank.save()
                return redirect('student_dashboard')
        else:
            areaform = StudentsAreaOfInterestsForm()

    elif myuser.groups.filter(name='Supervisors'):
        mysupervisor = Supervisors.objects.get(staff=myuser)
        print(mysupervisor)
        if request.method == 'POST':
            areaform = SupervisorsAreaOfInterestsForm(request.POST)
            if areaform.is_valid():
                arearank = areaform.save(commit=False)
                arearank.supervisor = mysupervisor
                messages.success(request, f'Area of Interest saved!')
                arearank.save()
                return redirect('super_dashboard')
        else:
            areaform = StudentsAreaOfInterestsForm()  

    else:
        messages.success(request, f'You are not supervisor or student')
        return redirect('login')    
    context = {
        'areaform': areaform,
    }
    return render(request, 'accounts/rank_area.html', context)

@login_required
def updaterankarea(request, id):
    myuser = request.user
    myarearank = StudentsAreaOfInterests.objects.get(user=myuser)
    areaform = StudentsAreaOfInterestsForm(instance=myarearank)
    if request.method == 'POST':
        areaform = StudentsAreaOfInterestsForm(request.POST, instance=myarearank)
        if areaform.is_valid():
            messages.success(request, f'Area of Interest has been updated!')
            areaform.save()
            return redirect('student_dashboard')
    context = {
        'areaform': areaform
    }
    return render(request, 'accounts/rank_area.html', context)

#Admin Links
@login_required
def admin_dashboard(request):
    myuser = request.user

    # initializing all tables
    mystudents = Students.objects.all()
    mysupervisors = Supervisors.objects.all()
    unallocated_students = UnallocatedStudents.objects.all()
    unallocated_supervisors = UnallocatedSupervisors.objects.all()

    # User counts
    unallocated_students_count  = unallocated_students.count()
    unallocated_supervisors_count =  unallocated_supervisors.count()
    mystudents_count = mystudents.count()
    mysupervisors_count = mysupervisors.count()

    # passing context to html template
    context = {
        'mystudents_count': mystudents_count,
        'mysupervisors_count': mysupervisors_count,
        'unallocated_supervisors_count': unallocated_supervisors_count,
        'unallocated_students_count': unallocated_students_count,
        'myuser': myuser
     }
    return render(request, 'accounts/admin/admin.html', context)

@login_required
def allocate(request):

    context ={}
    return render(request, 'accounts/admin/allocate.html', context)

@login_required
def allocate_results(request):

    context ={}
    return render(request, 'accounts/admin/allocate_results.html', context)

@login_required
def add_students(request):

    context ={}
    return render(request, 'accounts/admin/add_students.html', context)

@login_required
def add_supervisors(request):

    context ={}
    return render(request, 'accounts/admin/add_supervisors.html', context)

@login_required
def reg_deadline(request):
    if request.method == 'POST':
            regform = RegDeadlineForm(request.POST)
            if regform.is_valid():
                regform.save()
                messages.success(request,'Successfully set registration deadlines!')
                return redirect('admin_dashboard')
    else:
        regform = RegDeadlineForm()

    context = {
        'regform': regform
    }
    return render(request, 'accounts/admin/reg_deadline.html', context)

@login_required
def total_students(request):
    mystudents = Students.objects.all()
    mystudents_count = mystudents.count()

    context ={
        'mystudents' : mystudents,
        'mystudents_count' : mystudents_count
    }
    return render(request, 'accounts/admin/total_students.html', context)

@login_required
def total_supervisors(request):
    mysupervisors = Supervisors.objects.all()
    mysupervisors_count = mysupervisors.count()

    context ={
        'mysupervisors' : mysupervisors,
        'mysupervisors_count': mysupervisors_count
    }
    return render(request, 'accounts/admin/total_supervisors.html', context)

@login_required
def unallocated_students(request):
    mystudents = UnallocatedStudents.objects.all()
    mystudents_count = mystudents.count()

    context ={
        'mystudents' : mystudents,
        'mystudents_count' : mystudents_count
    }
    return render(request, 'accounts/admin/unallocated_students.html', context)

@login_required
def unallocated_supervisors(request):
    mysupervisors = UnallocatedSupervisors.objects.all()
    mysupervisors_count = mysupervisors.count()

    context ={
        'mysupervisors' : mysupervisors,
        'mysupervisors_count': mysupervisors_count
    }

    return render(request, 'accounts/admin/unallocated_supervisors.html', context)

@login_required
def set_constraints(request):
    if request.method == 'POST':
        setform = SupervisorsConstraintForm(request.POST)
        if setform.is_valid():
            setform.save()
            messages.success(request,'Successfully set supervisor constraints!')
            return redirect('admin_dashboard')
    else:
        setform = SupervisorsConstraintForm()

    context = {
        'setform': setform
    }
    return render(request, 'accounts/admin/set_constraints.html', context)