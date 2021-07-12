# Generated by Django 3.2.4 on 2021-07-09 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_alter_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_level', models.CharField(choices=[('Professor', 'Professor'), ('Associate Professor', 'Associate Professor'), ('Senior Lecturer', 'Senior Lecturer'), ('Lecturer 1', 'Lecturer 1'), ('Lecturer 2', 'Lecturer 2'), ('Assistant Lecturer', 'Assistant Lecturer')], max_length=200)),
                ('department', models.CharField(choices=[('CIS', 'Computer and Information Science')], max_length=200)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('400', '400 Level'), ('500', '500 Level')], max_length=200)),
                ('department', models.CharField(choices=[('CIS', 'Computer and Information Science')], max_length=200)),
                ('course', models.CharField(choices=[('Computer Science', 'Computer Science'), ('MIS', 'Management and Information Science')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Research', 'Research'), ('Implementation', 'Implementation'), ('Research + Implementation', 'Research + Implementation')], max_length=200, null=True, verbose_name='Category of Project')),
                ('first_choice', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, unique=True, verbose_name='First Choice')),
                ('second_choice', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, unique=True, verbose_name='Second Choice')),
                ('third_choice', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, unique=True, verbose_name='Third Choice')),
                ('fourth_choice', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, unique=True, verbose_name='Fourth Choice')),
                ('fifth_choice', models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, unique=True, verbose_name='Fifth Choice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Account')),
            ],
        ),
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Unallocated', 'Unallocated'), ('Allocated', 'Allocated')], max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.supervisor')),
            ],
        ),
    ]
