from django.shortcuts import render, redirect
#import django default form for user creation
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
            return redirect('login')
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
    context = {}
    return render(request, 'accounts/usertype.html', context)

@login_required
def student_info(request):
    context = {}
    return render(request, 'accounts/studentinfo.html', context)

@login_required
def supervisor_info(request):
    context = {}
    return render(request, 'accounts/supervisorinfo.html', context)

@login_required
def super_dashboard(request):
    context = {}
    return render(request, 'accounts/supervisordashboard.html', context)

@login_required
def student_dashboard(request):
    context = {}
    return render(request, 'accounts/studentdashboard.html', context)