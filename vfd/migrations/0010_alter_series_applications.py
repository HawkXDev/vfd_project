# Generated by Django 4.0.6 on 2022-09-14 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0009_alter_series_applications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='applications',
            field=models.ManyToManyField(to='vfd.application', verbose_name='Применения'),
        ),
    ]
