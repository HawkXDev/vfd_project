# Generated by Django 4.0.6 on 2022-09-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0172_alter_frequencydrive_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='cooling_fan_control',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (20, 'Да')], null=True, verbose_name='Управление вентилятором охлаждения'),
        ),
    ]
