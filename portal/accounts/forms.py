from django.contrib.auth.forms import UserCreationForm 
from django import forms
#import django admin user model
from django.contrib.auth.models import User

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