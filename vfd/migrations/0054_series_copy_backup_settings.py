# Generated by Django 4.0.6 on 2022-09-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0053_series_pre_configurations_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='copy_backup_settings',
            field=models.BooleanField(default=False, verbose_name='Возможность копирования/бэкапа настроек'),
        ),
    ]
