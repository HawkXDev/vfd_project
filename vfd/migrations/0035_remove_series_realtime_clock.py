# Generated by Django 4.0.6 on 2022-09-14 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0034_alter_series_additional_communications_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='realtime_clock',
        ),
    ]
