# Generated by Django 4.0.6 on 2022-09-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0075_alter_series_operating_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='sto_function',
            field=models.BooleanField(blank=True, null=True, verbose_name='Функция STO (функция безопасной остановки)'),
        ),
    ]
