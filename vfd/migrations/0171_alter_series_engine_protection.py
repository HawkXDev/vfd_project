# Generated by Django 4.0.6 on 2022-09-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0170_remove_series_main_control_functions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='engine_protection',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Перегрузка по току, перенапряжение, перегрев, потеря фазы и др.')], null=True, verbose_name='Защита двигателя'),
        ),
    ]
