# Generated by Django 3.2.4 on 2021-07-16 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.students')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.supervisors')),
            ],
            options={
                'verbose_name_plural': 'Allocated',
            },
        ),
        migrations.CreateModel(
            name='StudentRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fifth_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fifth_choice', to='accounts.supervisors', verbose_name='Fifth Choice Supervisor')),
                ('first_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_choice', to='accounts.supervisors', verbose_name='First Choice Supervisor')),
                ('fourth_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fourth_choice', to='accounts.supervisors', verbose_name='Fourth Choice Supervisor')),
                ('second_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_choice', to='accounts.supervisors', verbose_name='Second Choice Supervisor')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.students', verbose_name='Student Account')),
                ('third_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_choice', to='accounts.supervisors', verbose_name='Third Choice Supervisor')),
            ],
            options={
                'verbose_name_plural': 'Student Ranking',
            },
        ),
        migrations.CreateModel(
            name='SupervisorRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fifth_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fifth_choice', to='accounts.students', verbose_name='Fifth Choice Student')),
                ('first_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_choice', to='accounts.students', verbose_name='First Choice Student')),
                ('fourth_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fourth_choice', to='accounts.students', verbose_name='Fourth Choice Student')),
                ('second_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_choice', to='accounts.students', verbose_name='Second Choice Student')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.supervisors', verbose_name='Supervisor Account')),
                ('third_choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_choice', to='accounts.students', verbose_name='Third Choice Student')),
            ],
            options={
                'verbose_name_plural': 'Student Ranking',
            },
        ),
        migrations.CreateModel(
            name='UnallocatedStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.students')),
            ],
            options={
                'verbose_name_plural': 'Unallocated Students',
            },
        ),
        migrations.CreateModel(
            name='UnallocatedSupervisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.supervisors')),
            ],
            options={
                'verbose_name_plural': 'Unallocated Supervisors',
            },
        ),
        migrations.DeleteModel(
            name='Allocation',
        ),
    ]
