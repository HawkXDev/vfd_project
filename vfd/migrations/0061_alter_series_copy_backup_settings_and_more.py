# Generated by Django 4.0.6 on 2022-09-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0060_series_fire_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='copy_backup_settings',
            field=models.BooleanField(blank=True, null=True, verbose_name='Возможность копирования/бэкапа настроек'),
        ),
        migrations.AlterField(
            model_name='series',
            name='encoder_support',
            field=models.BooleanField(blank=True, null=True, verbose_name='Подключение энкодера'),
        ),
    ]
