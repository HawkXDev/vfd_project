# Generated by Django 4.0.6 on 2022-09-14 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0025_remove_series_control_built_in_fan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='overcurrent_protection',
        ),
        migrations.RemoveField(
            model_name='series',
            name='overvoltage_protection',
        ),
        migrations.RemoveField(
            model_name='series',
            name='temperature_protection',
        ),
    ]
