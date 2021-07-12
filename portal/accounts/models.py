from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Profiles(models.Model):
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
    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return str(self.user) + " is a " + str(self.user_type)
class AreaOfInterests(models.Model):
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

    user = models.OneToOneField(User, verbose_name=("User Account"), on_delete=models.CASCADE, primary_key=True)
    type = models.CharField(max_length=200, verbose_name=("Category of Project"), choices=CATEGORY, null=True)
    first_choice = models.CharField(max_length=200, verbose_name=("First Choice"), choices=AREAS, null=True)
    second_choice = models.CharField(max_length=200, verbose_name=("Second Choice"), choices=AREAS, null=True)
    third_choice = models.CharField(max_length=200, verbose_name=("Third Choice"), choices=AREAS, null=True)
    fourth_choice = models.CharField(max_length=200, verbose_name=("Fourth Choice"), choices=AREAS, null=True)
    fifth_choice = models.CharField(max_length=200, verbose_name=("Fifth Choice"), choices=AREAS, null=True)

    class Meta:
        verbose_name_plural = 'Area of Interests'

class Students(models.Model):
    LEVEL = (
        ('400', '400 Level'),
        ('500', '500 Level'),
    )
    DEPARTMENT = (
        ('CIS', 'Computer and Information Science'),
    )
    COURSE = (
        ('Computer Science', 'Computer Science'),
        ('MIS', 'Management and Information Science'),
    )

    student = models.OneToOneField(User, on_delete=models.CASCADE, null=False, primary_key=True)
    level = models.CharField(max_length=200, choices=LEVEL)
    department = models.CharField(max_length=200, choices=DEPARTMENT)
    course = models.CharField(max_length=200, choices=COURSE)
    class Meta:
        verbose_name_plural = 'Students'

class Supervisors(models.Model):
    LEVEL = (
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Senior Lecturer', 'Senior Lecturer'),
        ('Lecturer 1', 'Lecturer 1'),
        ('Lecturer 2', 'Lecturer 2'),
        ('Assistant Lecturer', 'Assistant Lecturer'),
    )
    DEPARTMENT = (
        ('CIS', 'Computer and Information Science'),
    )

    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=False, primary_key=True)
    staff_level = models.CharField(max_length=200, choices=LEVEL)
    department = models.CharField(max_length=200, choices=DEPARTMENT)

    class Meta:
        verbose_name_plural = 'Supervisors'


class Allocation(models.Model):
    STATUS = (
        ('Unallocated', 'Unallocated'),
        ('Allocated', 'Allocated'),
    )

    student = models.OneToOneField(Students,  on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=200, choices=STATUS)
    supervisor = models.ForeignKey(Supervisors, on_delete=models.CASCADE, null=False)

class Meta:
        verbose_name_plural = 'Allocation'
