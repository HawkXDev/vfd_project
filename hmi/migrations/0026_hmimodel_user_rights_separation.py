# Generated by Django 4.0.6 on 2022-12-28 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0025_hmimodel_communication_drivers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmimodel',
            name='user_rights_separation',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, 'Да, 8 уровней паролей и 8 аккаунтов')], null=True, verbose_name='Разделение прав пользователя'),
        ),
    ]
