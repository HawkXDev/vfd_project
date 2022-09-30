# Generated by Django 4.0.6 on 2022-09-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0148_alter_series_control_methods'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='carrier_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '0.5...16')], null=True, verbose_name='Несущая частота ШИМ, кГц'),
        ),
    ]
