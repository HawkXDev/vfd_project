# Generated by Django 4.0.6 on 2022-09-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0023_alter_series_engine_cascade_control_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='different_engines_work',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'До 4 независимых групп параметров двигателя')], null=True, verbose_name='Работа с разными двигателями'),
        ),
    ]
