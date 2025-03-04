# Generated by Django 4.0.6 on 2022-09-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0137_alter_series_brake_interrupter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='skip_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (10, 'Пропуск одной полосы частот'), (20, 'Пропуск 2-х полос частот'), (30, 'Пропуск 3-х полос частот'), (40, 'Пропуск 4-х полос частот')], null=True, verbose_name='Пропуск критических частот'),
        ),
    ]
