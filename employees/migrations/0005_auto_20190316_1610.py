# Generated by Django 2.1.7 on 2019-03-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('employees', '0004_auto_20190316_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='department',
            table=None,
        ),
        migrations.AlterModelTable(
            name='employees',
            table=None,
        ),
        migrations.AlterModelTable(
            name='position',
            table=None,
        ),
    ]