# Generated by Django 4.0.6 on 2022-12-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0015_hmimodel_speaker'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmimodel',
            name='audio_output',
            field=models.BooleanField(blank=True, null=True, verbose_name='Аудио выход'),
        ),
    ]
