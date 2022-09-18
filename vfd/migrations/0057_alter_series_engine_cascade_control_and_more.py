# Generated by Django 4.0.6 on 2022-09-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0056_alter_series_starting_torque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='engine_cascade_control',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Нет'), (2, 'Да, до 4 двигателей'), (3, 'Да, до 8 двигателей')], null=True, verbose_name='Управление каскадом двигателей'),
        ),
        migrations.AlterField(
            model_name='series',
            name='multi_pump_system',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Нет'), (2, 'Да, до 4 насосов'), (3, 'Да, до 8 насосов')], null=True, verbose_name='Много-насосный режим'),
        ),
    ]
