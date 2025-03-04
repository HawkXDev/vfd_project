# Generated by Django 4.0.6 on 2022-09-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0036_alter_series_external_power_24v'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='protection_degree',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'IP20'), (2, 'IP21'), (3, 'IP55')], null=True, verbose_name='Степень защиты'),
        ),
    ]
