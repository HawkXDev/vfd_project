# Generated by Django 4.0.6 on 2022-09-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0007_alter_series_analog_inputs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='emc_filter',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'C3'), (2, 'C2')], null=True, verbose_name='Встроенный EMC фильтр'),
        ),
    ]
