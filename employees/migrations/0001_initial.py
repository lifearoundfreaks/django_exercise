# Generated by Django 2.2.1 on 2019-05-19 12:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('base_salary', models.IntegerField(default=0)),
                ('boss_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.Position')),
            ],
            options={
                'db_table': 'Position',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('hiring_date', models.DateField(default=datetime.date.today)),
                ('additional_salary', models.IntegerField(default=0)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Position')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
