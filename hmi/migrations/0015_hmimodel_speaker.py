# Generated by Django 4.0.6 on 2022-12-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0014_hmimodel_sd_card_alter_hmimodel_flash_rom'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmimodel',
            name='speaker',
            field=models.BooleanField(blank=True, null=True, verbose_name='Динамик'),
        ),
    ]
