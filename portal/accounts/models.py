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

    def __str__(self):
        return str(self.user)
class AreaOfInterest(models.Model):
    AREAS = (
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('Internet of Things (IOT)', 'Internet of Things (IOT)'),
        ('Software Engineering', 'Software Engineering'),
        ('Computer Hardware', 'Computer Hardware'),
        ('Algorithms', 'Algorithms'),
        ('Cloud Computing', 'Cloud Computing'),
        ('Networking and Communication', 'Networking and Communication'),
        ('Data Science', 'Data Science'),
        ('UI/UX Design','UI/UX Design'),
        ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'),
        ('Machine Learning', 'Machine Learning'),
        ('Cyber Security', 'Cyber Security'),
        ('Information Systems','Information Systems'),
        ('Digital / Interactive Media', 'Digital / Interactive Media'),
        ('Game Design','Game Design'),
        ('Computer Graphics', 'Computer Graphics'),
        ('Web Development', 'Web Development'),
        ('Bioinformatics','Bioinformatics'),
        ('Database Management', 'Database Management'),
        ('Mobile Development','Mobile Development'),
    )
    CATEGORY = (
        ('Research', 'Research'),
        ('Implementation', 'Implementation'),
        ('Research + Implementation', 'Research + Implementation'),
    )

    user = models.OneToOneField(User, verbose_name=("User Account"), on_delete=models.CASCADE)
    type = models.CharField(max_length=200, verbose_name=("Category of Project"), choices=CATEGORY, null=True)
    first_choice = models.CharField(max_length=200, verbose_name=("First Choice"), choices=AREAS, null=True, unique=True)
    second_choice = models.CharField(max_length=200, verbose_name=("Second Choice"), choices=AREAS, null=True, unique=True)
    third_choice = models.CharField(max_length=200, verbose_name=("Third Choice"), choices=AREAS, null=True, unique=True)
    fourth_choice = models.CharField(max_length=200, verbose_name=("Fourth Choice"), choices=AREAS, null=True, unique=True)
    fifth_choice = models.CharField(max_length=200, verbose_name=("Fifth Choice"), choices=AREAS, null=True, unique=True)