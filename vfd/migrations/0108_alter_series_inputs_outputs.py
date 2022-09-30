# Generated by Django 4.0.6 on 2022-09-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0107_alter_series_operating_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='inputs_outputs',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'DI: 4; AI: 1; TO: 0; RO: 1; AO: 1'), (20, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'), (30, 'DI: 5; AI: 1; TO: 1; RO: 1; AO: 1'), (40, 'DI: 6; AI: 2; TO: 0; RO: 1; AO: 1'), (50, 'DI: 6; AI: 2; TO: 1; RO: 2; AO: 2'), (60, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'), (70, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2')], null=True, verbose_name='Входы/выходы'),
        ),
    ]
