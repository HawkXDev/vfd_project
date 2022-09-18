# Generated by Django 4.0.6 on 2022-09-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0057_alter_series_engine_cascade_control_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='stop_prevention',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Токоограничение при разгоне, замедлении и работе')], null=True, verbose_name='Предотвращение перегрузки (токоограничение)'),
        ),
    ]
