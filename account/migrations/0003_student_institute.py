# Generated by Django 3.0.1 on 2020-05-06 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
        ('account', '0002_auto_20200505_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='institute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='std_inst', to='institute.Institute'),
        ),
    ]
