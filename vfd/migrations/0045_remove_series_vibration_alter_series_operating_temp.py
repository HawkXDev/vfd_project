# Generated by Django 4.0.6 on 2022-09-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0044_remove_series_installation_place_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='vibration',
        ),
        migrations.AlterField(
            model_name='series',
            name='operating_temp',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '-10...+40(+50); Со снижением характеристик -10...+60'), (2, '-20...+50; Со снижением характеристик -20...+60')], null=True, verbose_name='Рабочая температура, ℃'),
        ),
    ]
