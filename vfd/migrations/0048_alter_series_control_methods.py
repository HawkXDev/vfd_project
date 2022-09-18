# Generated by Django 4.0.6 on 2022-09-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0047_alter_series_control_methods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='control_methods',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, 'V/F (скалярное управление), \nSVC (бездатчиковое векторное управление)'), (11, 'V/F (скалярное управление), \nFVC (векторное управление потоком)')], null=True, verbose_name='Методы управления'),
        ),
    ]
