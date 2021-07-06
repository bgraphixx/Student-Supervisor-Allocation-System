from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Profile(models.Model):
    GENDER = (
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Non-binary', 'Non-binary'),
            ('Prefer not to say', 'Prefer not to say'),
        )
    TYPE = (
        ('Student', 'Student'),
        ('Supervisor', 'Supervisor'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=200,  choices=TYPE, null=True)
    gender = models.CharField(max_length=200, choices=GENDER, null=True)