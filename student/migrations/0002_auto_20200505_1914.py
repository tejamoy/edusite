# Generated by Django 3.0.1 on 2020-05-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screcord',
            name='course',
            field=models.ManyToManyField(related_name='screcord', to='course.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(related_name='sc_crse_reg', to='course.Course'),
        ),
    ]
