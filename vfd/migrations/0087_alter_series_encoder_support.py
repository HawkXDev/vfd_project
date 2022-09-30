# Generated by Django 4.0.6 on 2022-09-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0086_remove_series_additional_communications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='encoder_support',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Импульсный вход'), (2, 'Плата расширения энкодера (ABZ, UVW, Rotary transformer)')], null=True, verbose_name='Подключение энкодера'),
        ),
    ]
