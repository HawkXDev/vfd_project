# Generated by Django 4.0.6 on 2022-09-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0168_series_removable_control_panel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='control_panel_desc',
        ),
        migrations.AddField(
            model_name='series',
            name='potentiometer',
            field=models.BooleanField(blank=True, null=True, verbose_name='Потенциометр'),
        ),
    ]
