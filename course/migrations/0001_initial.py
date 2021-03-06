# Generated by Django 3.0.1 on 2020-05-05 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('account', '0001_initial'),
        ('dptclass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ce_abb', models.CharField(default='None', max_length=20, unique=True)),
                ('ce_name', models.CharField(max_length=100)),
                ('ce_dptcls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dptclass.DptClass')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('teacher', models.ManyToManyField(to='account.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('student', models.ManyToManyField(to='student.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('screcord', models.ManyToManyField(to='student.SCRecord')),
            ],
        ),
    ]
