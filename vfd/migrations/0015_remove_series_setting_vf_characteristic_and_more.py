# Generated by Django 4.0.6 on 2022-09-14 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0014_alter_series_control_panel_at_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='setting_vf_characteristic',
        ),
        migrations.RemoveField(
            model_name='series',
            name='speed_control_range',
        ),
    ]
