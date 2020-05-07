# Generated by Django 3.0.1 on 2020-05-05 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DptClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_abb', models.CharField(default='None', max_length=20)),
                ('dcls_name', models.CharField(max_length=100)),
                ('dcls_dpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department')),
            ],
        ),
    ]
