# Generated by Django 3.2.4 on 2021-07-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210710_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaofinterests',
            name='fifth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, verbose_name='Fifth Choice'),
        ),
        migrations.AlterField(
            model_name='areaofinterests',
            name='first_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, verbose_name='First Choice'),
        ),
        migrations.AlterField(
            model_name='areaofinterests',
            name='fourth_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, verbose_name='Fourth Choice'),
        ),
        migrations.AlterField(
            model_name='areaofinterests',
            name='second_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, verbose_name='Second Choice'),
        ),
        migrations.AlterField(
            model_name='areaofinterests',
            name='third_choice',
            field=models.CharField(choices=[('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things (IOT)', 'Internet of Things (IOT)'), ('Software Engineering', 'Software Engineering'), ('Computer Hardware', 'Computer Hardware'), ('Algorithms', 'Algorithms'), ('Cloud Computing', 'Cloud Computing'), ('Networking and Communication', 'Networking and Communication'), ('Data Science', 'Data Science'), ('UI/UX Design', 'UI/UX Design'), ('Human Computer Interaction (HCI)', 'Human Computer Interaction (HCI)'), ('Machine Learning', 'Machine Learning'), ('Cyber Security', 'Cyber Security'), ('Information Systems', 'Information Systems'), ('Digital / Interactive Media', 'Digital / Interactive Media'), ('Game Design', 'Game Design'), ('Computer Graphics', 'Computer Graphics'), ('Web Development', 'Web Development'), ('Bioinformatics', 'Bioinformatics'), ('Database Management', 'Database Management'), ('Mobile Development', 'Mobile Development')], max_length=200, null=True, verbose_name='Third Choice'),
        ),
    ]
