# Generated by Django 2.2.1 on 2019-05-19 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20190316_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('works_Data', models.DateField()),
                ('salary', models.FloatField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.RemoveField(
            model_name='employees',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='position',
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.Position'),
        ),
    ]
