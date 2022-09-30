# Generated by Django 4.0.6 on 2022-09-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0078_alter_series_choke_dc_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='choke_dc_link',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Опция'), (2, 'Встроен на мощности от 45 кВт'), (3, 'Встроен на мощности 11, 15 кВт и от 200 кВт')], null=True, verbose_name='Дроссель в звене постоянного тока'),
        ),
    ]
