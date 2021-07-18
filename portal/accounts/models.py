from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_full_name(self):
    return str(self.first_name) + " " + str(self.last_name)

User.add_to_class("__str__", get_full_name)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    user_type = models.CharField(max_length=200,  choices=TYPE)
    gender = models.CharField(max_length=200, choices=GENDER)
    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return str(self.user) + " is a " + str(self.gender) + " " + str(self.user_type)

class Administrators(models.Model):
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

    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    staff_level = models.CharField(max_length=200, choices=LEVEL)
    department = models.CharField(max_length=200, choices=DEPARTMENT)

    class Meta:
        verbose_name_plural = 'Administrators'

    def __str__(self):
        return str(self.staff)

class Students(models.Model):
    LEVEL = (
        ('400 Level', '400 Level'),
        ('500 Level', '500 Level'),
    )
    DEPARTMENT = (
        ('CIS', 'Computer and Information Science'),
    )
    COURSE = (
        ('Computer Science', 'Computer Science'),
        ('Management and Information Science', 'Management and Information Science'),
    )

    student = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    level = models.CharField(max_length=200, choices=LEVEL)
    department = models.CharField(max_length=200, choices=DEPARTMENT)
    course = models.CharField(max_length=200, choices=COURSE)
    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self):
        return str(self.student)

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

    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    staff_level = models.CharField(max_length=200, choices=LEVEL)
    department = models.CharField(max_length=200, choices=DEPARTMENT)

    class Meta:
        verbose_name_plural = 'Supervisors'

    def __str__(self):
        return str(self.staff)

class SupervisorsAreaOfInterests(models.Model):
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

    supervisor = models.OneToOneField(Supervisors, verbose_name=("Supervisor"), on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=200, verbose_name=("Category of Project"), choices=CATEGORY)
    first_choice = models.CharField(max_length=200, verbose_name=("First Choice"), choices=AREAS)
    second_choice = models.CharField(max_length=200, verbose_name=("Second Choice"), choices=AREAS)
    third_choice = models.CharField(max_length=200, verbose_name=("Third Choice"), choices=AREAS)
    fourth_choice = models.CharField(max_length=200, verbose_name=("Fourth Choice"), choices=AREAS)
    fifth_choice = models.CharField(max_length=200, verbose_name=("Fifth Choice"), choices=AREAS)

    class Meta:
        verbose_name_plural = 'Supervisors Area of Interests'

class StudentsAreaOfInterests(models.Model):
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

    student = models.OneToOneField(Students, verbose_name=("Student"), on_delete=models.CASCADE, null=False)
    type = models.CharField(max_length=200, verbose_name=("Category of Project"), choices=CATEGORY)
    first_choice = models.CharField(max_length=200, verbose_name=("First Choice"), choices=AREAS)
    second_choice = models.CharField(max_length=200, verbose_name=("Second Choice"), choices=AREAS)
    third_choice = models.CharField(max_length=200, verbose_name=("Third Choice"), choices=AREAS)
    fourth_choice = models.CharField(max_length=200, verbose_name=("Fourth Choice"), choices=AREAS)
    fifth_choice = models.CharField(max_length=200, verbose_name=("Fifth Choice"), choices=AREAS)

    class Meta:
        verbose_name_plural = 'Students Area of Interests'

# class StudentRanking(models.Model):
#     student = models.OneToOneField(Students, verbose_name=("Student Account"), on_delete=models.CASCADE, null=False)
#     first_choice = models.ForeignKey(Supervisors, verbose_name=("First Choice Supervisor"), on_delete=models.CASCADE, null=False, related_name="first_choice")
#     second_choice = models.ForeignKey(Supervisors, verbose_name=("Second Choice Supervisor"), on_delete=models.CASCADE, null=False, related_name="second_choice")
#     third_choice = models.ForeignKey(Supervisors, verbose_name=("Third Choice Supervisor"), on_delete=models.CASCADE, null=False, related_name="third_choice")
#     fourth_choice = models.ForeignKey(Supervisors, verbose_name=("Fourth Choice Supervisor"), on_delete=models.CASCADE, null=False, related_name="fourth_choice")
#     fifth_choice = models.ForeignKey(Supervisors, verbose_name=("Fifth Choice Supervisor"), on_delete=models.CASCADE, null=False, related_name="fifth_choice")

#     class Meta:
#         verbose_name_plural = 'Student Ranking'

#     def __str__(self):
#         return "['"+ str(self.student) + "' , '" + str(self.first_choice) + "' , '" + str(self.second_choice) + "' , '" + str(self.third_choice) + "' , '" + str(self.fourth_choice) + "' , '" + str(self.fifth_choice) + "']"

# class SupervisorRanking(models.Model):
#     supervisor = models.OneToOneField(Supervisors, verbose_name=("Supervisor Account"), on_delete=models.CASCADE, null=False)
#     first_choice = models.ForeignKey(Students, verbose_name=("First Choice Student"), on_delete=models.CASCADE, null=False, related_name="first_choice")
#     second_choice = models.ForeignKey(Students, verbose_name=("Second Choice Student"), on_delete=models.CASCADE, null=False, related_name="second_choice")
#     third_choice = models.ForeignKey(Students, verbose_name=("Third Choice Student"), on_delete=models.CASCADE, null=False, related_name="third_choice")
#     fourth_choice = models.ForeignKey(Students, verbose_name=("Fourth Choice Student"), on_delete=models.CASCADE, null=False, related_name="fourth_choice")
#     fifth_choice = models.ForeignKey(Students, verbose_name=("Fifth Choice Student"), on_delete=models.CASCADE, null=False, related_name="fifth_choice")

#     class Meta:
#         verbose_name_plural = 'Supervisor Ranking'

#     def __str__(self):
#         return "['"+ str(self.supervisor) + "' , '" + str(self.first_choice) + "' , '" + str(self.second_choice) + "' , '" + str(self.third_choice) + "' , '" + str(self.fourth_choice) + "' , '" + str(self.fifth_choice) + "']"

class SupervisorContraints(models.Model):
    professor = models.IntegerField(verbose_name='Professor')
    assoc_professor = models.IntegerField(verbose_name='Associate Professor')
    senior_lect = models.IntegerField(verbose_name='Senior Lecturer')
    lect_one = models.IntegerField(verbose_name='Lecturer 1')
    lect_two = models.IntegerField(verbose_name='Lecturer 2')
    assist = models.IntegerField(verbose_name='Assistant Lecturer')

    class Meta:
        verbose_name_plural = 'Supervisor Constraints'

class RegDeadline(models.Model):
    area_of_interest = models.DateField(verbose_name='Area of Interest')
    ranking = models.DateField(verbose_name='Ranking')
    submit_profile = models.DateField(verbose_name='Submit Profile')
    allocation_result = models.DateField(verbose_name='Allocation Result')
    class Meta:
        verbose_name_plural = 'Registration Deadlines'

class Allocated(models.Model):
    student = models.OneToOneField(Students,  on_delete=models.CASCADE, null=False)
    supervisor = models.ForeignKey(Supervisors, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Allocated'

    def __str__(self):
        return str(self.student) + " is allocated to " + str(self.supervisor)

class UnallocatedStudents(models.Model):
    student = models.OneToOneField(Students,  on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Unallocated Students'

    def __str__(self):
        return str(self.student)

class UnallocatedSupervisors(models.Model):
    supervisor = models.OneToOneField(Supervisors, on_delete=models.CASCADE, null=False)
    class Meta:
        verbose_name_plural = 'Unallocated Supervisors'

    def __str__(self):
        return str(self.supervisor)
