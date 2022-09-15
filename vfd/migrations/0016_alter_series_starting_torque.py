# Generated by Django 4.0.6 on 2022-09-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0015_remove_series_setting_vf_characteristic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='starting_torque',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'V/F (скалярное управление), SVC (бездатчиковое векторное управление)')], null=True, verbose_name='Пусковой момент'),
        ),
    ]
