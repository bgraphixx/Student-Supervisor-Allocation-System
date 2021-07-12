from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.forms import ModelForm
#import django admin user model
from django.contrib.auth.models import User
from .models import *
class CreateUserForm(UserCreationForm):
    #Change placeholder for stubborn fields like username, password1 and password2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':('Enter First Name')})
        self.fields['last_name'].widget.attrs.update({'placeholder':('Enter Last Name')})
        self.fields['email'].widget.attrs.update({'placeholder':('Enter Email Address')})
        self.fields['username'].widget.attrs.update({'placeholder':('Enter Matric/Staff Number')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Enter your Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Confirm your password')})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']

class AreaOfInterestsForm(ModelForm):
    class Meta:
        model = AreaOfInterests
        fields = ('type', 'first_choice', 'second_choice', 'third_choice', 'fourth_choice', 'fifth_choice')
        labels = {
            'type' : 'What kind of project do you preferred?',
            'first_choice' : 'First Choice Project Area',
            'second_choice' : 'Second Choice Project Area',
            'third_choice' : 'Third Choice Project Area',
            'fourth_choice' : 'Fourth Choice Project Area',
            'fifth_choice' : 'Fifth Choice Project Area',
        }

class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profiles
        fields = '__all__'
        labels = {
            'user_type' : 'Are you a student, supervisor or adminstrator?',
            'gender' : 'What is your gender?',
        }

class SupervisorForm(forms.ModelForm):
    class Meta: 
        model = Supervisors
        fields = '__all__'
        labels = {
            'staff_level' : 'What is your current position?',
            'department' : 'Which department do you belong to?',
        }

class StudentForm(forms.ModelForm):
    class Meta: 
        model = Students
        fields = '__all__'
        labels = {
            'level' : 'What is your current position?',
            'department' : 'Which department do you belong to?',
        }