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

class StudentsAreaOfInterestsForm(ModelForm):
    class Meta:
        model = StudentsAreaOfInterests
        fields = ('type', 'first_choice', 'second_choice', 'third_choice', 'fourth_choice', 'fifth_choice')
        labels = {
            'type' : 'What kind of project do you preferred?',
            'first_choice' : 'First Choice Project Area',
            'second_choice' : 'Second Choice Project Area',
            'third_choice' : 'Third Choice Project Area',
            'fourth_choice' : 'Fourth Choice Project Area',
            'fifth_choice' : 'Fifth Choice Project Area',
        }

class SupervisorsAreaOfInterestsForm(ModelForm):
    class Meta:
        model = SupervisorsAreaOfInterests
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
        fields = ('user_type', 'gender')
        labels = {
            'user_type' : 'Are you a student, supervisor or adminstrator?',
            'gender' : 'What is your gender?',
        }
        widgets = {
            'user_type': forms.Select(attrs={'class': 'formcontrol',}),
            'gender': forms.Select(attrs={'class': 'formcontrol',})
        }

class SupervisorForm(forms.ModelForm):
    class Meta: 
        model = Supervisors
        fields = ('staff_level', 'department')
        labels = {
            'staff_level' : 'What is your current position?',
            'department' : 'Which department do you belong to?',
        }
        widgets = {
            'staff_level': forms.Select(attrs={'class': 'formcontrol',}),
            'department': forms.Select(attrs={'class': 'formcontrol',})
        }

class StudentForm(forms.ModelForm):
    class Meta: 
        model = Students
        fields = ('level', 'department', 'course')
        labels = {
            'level' : 'What level are you in?',
            'department' : 'Which department do you belong to?',
            'course': 'Choose programme:',
        }
        widgets = {
            'level': forms.Select(attrs={'class': 'formcontrol',}),
            'department': forms.Select(attrs={'class': 'formcontrol',}),
            'course': forms.Select(attrs={'class': 'formcontrol',})
        }

class AdministratorForm(forms.ModelForm):
    class Meta: 
        model = Administrators
        fields = ('staff_level', 'department')
        labels = {
            'staff_level' : 'What is your current position?',
            'department' : 'Which department do you belong to?',
        }
        widgets = {
            'staff_level': forms.Select(attrs={'class': 'formcontrol',}),
            'department': forms.Select(attrs={'class': 'formcontrol',})
        }

class SupervisorsConstraintForm(forms.ModelForm):
    class Meta: 
        model = SupervisorContraints
        fields = ('professor','assoc_professor', 'senior_lect', 'lect_one', 'lect_two', 'assist')
        labels = {
            'professor' : 'Set Constraint for Professors:',
            'assoc_professor' : 'Set Constraints for Associate Professors:',
            'senior_lect' : 'Set Constraints for Senior Lecturers:',
            'lect_one' : 'Set Constraints for Lecturer 1:',
            'lect_two' : 'Set Constraints for Lecturer 2:',
            'assist' : 'Set Constraints for Assistant Lecturers:',
        }
        widgets = {
            'professor' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
            'assoc_professor' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
            'senior_lect' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
            'lect_one' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
            'lect_two' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
            'assist' : forms.NumberInput(attrs={'class': 'form-control mt-2 mb-2',}),
        }

class RegDeadlineForm(forms.ModelForm):
    class Meta: 
        model = RegDeadline
        fields = ('area_of_interest','ranking', 'submit_profile', 'allocation_result')
        labels = {
            'area_of_interest' : 'Set deadline for Area of Interest:',
            'ranking' : 'Set deadline for Ranking:',
            'submit_profile' : 'Set deadline for Submitting profile:',
            'allocation_result' : 'Set date to display allocation result:',
        }
        widgets = {
            'area_of_interest' : forms.DateInput(attrs={'class': 'form-control mt-2 mb-2', 'type':'date'}),
            'ranking' : forms.DateInput(attrs={'class': 'form-control mt-2 mb-2', 'type':'date'}),
            'submit_profile' : forms.DateInput(attrs={'class': 'form-control mt-2 mb-2', 'type':'date'}),
            'allocation_result' : forms.DateInput(attrs={'class': 'form-control mt-2 mb-2', 'type':'date'}),
        }