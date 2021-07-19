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
                myuser.groups.add(group)
                profile.user = myuser
                profile.save()
                return redirect('supervisor_info')
            elif profile.user_type == 'Admin':
                group = Group.objects.get(name='Administrators')
                myuser.groups.add(group)
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
    elif myuser.groups.filter(name='Administrators'):
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
        try: 
            mystudent = Students.objects.get(student=myuser)
            StudentsAreaOfInterests.objects.get(student=mystudent).delete()
        except:
            print('Area of Interest record of', mystudent ,'does not exist')
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
        try: 
            mysupervisor = Supervisors.objects.get(staff=myuser)
            StudentsAreaOfInterests.objects.get(student=mysupervisor).delete()
        except:
            print('Area of Interest record of', mysupervisor ,'does not exist')
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

def submit_profile(request):
    myuser = request.user
    if myuser.groups.filter(name ='Students'):
        mystudent = Students.objects.get(student = myuser)
        if StudentsAreaOfInterests.objects.filter(student = mystudent).exists():
            if UnallocatedStudents.objects.filter(student = mystudent).exists():
                messages.success(request, f'You have already submitted your profile')
            else:
                starea = StudentsAreaOfInterests.objects.get(student = mystudent)
                addstudent = UnallocatedStudents.objects.create(student = mystudent, level = mystudent.level, department = mystudent.department, course = mystudent.course, type = starea.type, first_choice = starea.first_choice, second_choice = starea.second_choice, third_choice = starea.third_choice, fourth_choice = starea.fourth_choice, fifth_choice = starea.fifth_choice)
                addstudent.save()
                messages.success(request, f'Your profile has been submitted')
        else: 
            messages.success(request, f'You have not set your area of interest')
        return redirect('student_dashboard')
    elif myuser.groups.filter(name='Supervisors'):
        mysupervisor = Supervisors.objects.get(staff = myuser)
        if SupervisorsAreaOfInterests.objects.filter(supervisor = mysupervisor).exists():
            if UnallocatedSupervisors.objects.filter(supervisor = mysupervisor).exists():
                messages.success(request, f'You have already submitted your profile')
            else:
                starea = SupervisorsAreaOfInterests.objects.get(supervisor = mysupervisor)
                addsuper = UnallocatedSupervisors.objects.create(supervisor = mysupervisor, staff_level = mysupervisor.staff_level, department = mysupervisor.department, type = starea.type, first_choice = starea.first_choice, second_choice = starea.second_choice, third_choice = starea.third_choice, fourth_choice = starea.fourth_choice, fifth_choice = starea.fifth_choice)
                addsuper.save()
                messages.success(request, f'Your profile has been submitted')
        else:
            messages.success(request, f'You have not set your area of interest')
        return redirect('super_dashboard')

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
    cons = SupervisorContraints.objects.all().exists()
    reg = RegDeadline.objects.all().exists()
    mysupervisors = UnallocatedSupervisors.objects.all()
    mysupervisors_count = mysupervisors.count()
    mystudents = UnallocatedStudents.objects.all()
    mystudents_count = mystudents.count()

    context = {
        'cons': cons,
        'reg' : reg,
        'mystudents_count': mystudents_count,
        'mysupervisors_count': mysupervisors_count,
    }
    return render(request, 'accounts/admin/allocate.html', context)

def checkpair(learn):
    exist = Allocated.objects.filter(student=learn).exists()
    return exist

def pair(learn, tut):
    allocatetable = Allocated.objects.all()
    allocatetable = Allocated(student = learn, supervisor = tut)
    allocatetable.save()

def stable_marriage(request):
    unsupervisors = UnallocatedSupervisors.objects.all()
    unstudents = UnallocatedStudents.objects.all()
    const = SupervisorContraints.objects.all()

    #grouping supervisors based on type and first choice

    ResearchAISuper = UnallocatedSupervisors.objects.filter(type="Research", first_choice = "Artificial Intelligence")
    ResearchSESuper = UnallocatedSupervisors.objects.filter(type="Research", first_choice = "Systems Engineering")
    ResearchNCSuper = UnallocatedSupervisors.objects.filter(type="Research", first_choice = "Networking and Communication")
    ResearchDASuper = UnallocatedSupervisors.objects.filter(type="Research", first_choice = "Design and Animation")
    ResearchCSSuper = UnallocatedSupervisors.objects.filter(type="Research", first_choice = "Cyber Security")

    ImplementAISuper = UnallocatedSupervisors.objects.filter(type="Implementation", first_choice = "Artificial Intelligence")
    ImplementSESuper = UnallocatedSupervisors.objects.filter(type="Implementation", first_choice = "Systems Engineering")
    ImplementNCSuper = UnallocatedSupervisors.objects.filter(type="Implementation", first_choice = "Networking and Communication")
    ImplementDASuper = UnallocatedSupervisors.objects.filter(type="Implementation", first_choice = "Design and Animation")
    ImplementCSSuper = UnallocatedSupervisors.objects.filter(type="Implementation", first_choice = "Cyber Security")

    ReImpAISuper = UnallocatedSupervisors.objects.filter(type="Research + Implementation", first_choice = "Artificial Intelligence")
    ReImpSESuper = UnallocatedSupervisors.objects.filter(type="Research + Implementation", first_choice = "Systems Engineering")
    ReImpNCSuper = UnallocatedSupervisors.objects.filter(type="Research + Implementation", first_choice = "Networking and Communication")
    ReImpDASuper = UnallocatedSupervisors.objects.filter(type="Research + Implementation", first_choice = "Design and Animation")
    ReImpCSSuper = UnallocatedSupervisors.objects.filter(type="Research + Implementation", first_choice = "Cyber Security")

    #grouping students based on type and first choice

    ResearchAIStudent = UnallocatedStudents.objects.filter(type="Research", first_choice = "Artificial Intelligence")
    ResearchSEStudent = UnallocatedStudents.objects.filter(type="Research", first_choice = "Systems Engineering")
    ResearchNCStudent = UnallocatedStudents.objects.filter(type="Research", first_choice = "Networking and Communication")
    ResearchDAStudent = UnallocatedStudents.objects.filter(type="Research", first_choice = "Design and Animation")
    ResearchCSStudent = UnallocatedStudents.objects.filter(type="Research", first_choice = "Cyber Security")

    ImplementAIStudent = UnallocatedStudents.objects.filter(type="Implementation", first_choice = "Artificial Intelligence")
    ImplementSEStudent = UnallocatedStudents.objects.filter(type="Implementation", first_choice = "Systems Engineering")
    ImplementNCStudent = UnallocatedStudents.objects.filter(type="Implementation", first_choice = "Networking and Communication")
    ImplementDAStudent = UnallocatedStudents.objects.filter(type="Implementation", first_choice = "Design and Animation")
    ImplementCSStudent = UnallocatedStudents.objects.filter(type="Implementation", first_choice = "Cyber Security")

    ReImpAIStudent = UnallocatedStudents.objects.filter(type="Research + Implementation", first_choice = "Artificial Intelligence")
    ReImpSEStudent = UnallocatedStudents.objects.filter(type="Research + Implementation", first_choice = "Systems Engineering")
    ReImpNCStudent = UnallocatedStudents.objects.filter(type="Research + Implementation", first_choice = "Networking and Communication")
    ReImpDAStudent = UnallocatedStudents.objects.filter(type="Research + Implementation", first_choice = "Design and Animation")
    ReImpCSStudent = UnallocatedStudents.objects.filter(type="Research + Implementation", first_choice = "Cyber Security")
    
    #allocate research students to research supervisors

    for supervisor in ResearchAISuper:
        for student in ResearchAIStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Artificial Intelligence" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ResearchSESuper:
        for student in ResearchSEStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Systems Engineering" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ResearchNCSuper:
        for student in ResearchNCStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Networking and Communication" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ResearchDASuper:
        for student in ResearchDAStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Design and Animation" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ResearchCSSuper:
        for student in ResearchCSStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Cyber Security" :
                    pair(student, supervisor)
                    student.delete()
    #allocate implementation students to implement supervisors

    for supervisor in ImplementAISuper:
        for student in ImplementAIStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Artificial Intelligence" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ImplementSESuper:
        for student in ImplementSEStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Systems Engineering" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ImplementNCSuper:
        for student in ImplementNCStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Networking and Communication" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ImplementDASuper:
        for student in ImplementDAStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Design and Animation" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ImplementCSSuper:
        for student in ImplementCSStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Cyber Security" :
                    pair(student, supervisor)
                    student.delete()

    #allocate research + implement students to research + implement supervisors

    for supervisor in ReImpAISuper:
        for student in ReImpAIStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Artificial Intelligence" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ReImpSESuper:
        for student in ReImpSEStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Systems Engineering" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ReImpNCSuper:
        for student in ReImpNCStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Networking and Communication" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ReImpDASuper:
        for student in ReImpDAStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Design and Animation" :
                    pair(student, supervisor)
                    student.delete()

    for supervisor in ReImpCSSuper:
        for student in ReImpCSStudent:
            if checkpair(student) == True:
                continue
            else:
                if student.first_choice == "Cyber Security" :
                    pair(student, supervisor)
                    student.delete()
    
    return redirect('allocate_results')

@login_required
def allocate_results(request):
    results = Allocated.objects.all()

    context = {
        'results': results
    }
    return render(request, 'accounts/admin/allocate_results.html', context)


@login_required
def add_students(request):

    context = {}
    return render(request, 'accounts/admin/add_students.html', context)

@login_required
def add_supervisors(request):

    context = {}
    return render(request, 'accounts/admin/add_supervisors.html', context)

@login_required
def reg_deadline(request):
    if request.method == 'POST':
            deadline = RegDeadline.objects.all()
            deadline.delete()
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
    setcons = SupervisorContraints.objects.all()
    setcons.delete()
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
