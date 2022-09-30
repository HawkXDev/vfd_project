# Generated by Django 4.0.6 on 2022-09-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0151_alter_series_carrier_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='carrier_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '0.5...16'), (31, '2...15'), (32, '2...15 (Default: 4)'), (33, '2...15/10/9 (Default: 8/6/4)'), (34, '2...16 (Default: 4/3)'), (35, '1...16/10/5 (Default: 6/4.5/3/1.8)'), (36, '2...12 (Default: 3)')], null=True, verbose_name='Несущая частота ШИМ, кГц'),
        ),
    ]
