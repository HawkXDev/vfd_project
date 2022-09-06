# Generated by Django 4.0.6 on 2022-09-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0028_series_setting_vf_characteristic'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='speed_control_range',
            field=models.FloatField(blank=True, null=True, verbose_name='Диапазон регулирования скорости, Гц'),
        ),
    ]
