# Generated by Django 4.0.6 on 2022-12-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0029_hmimodel_russian_software_hmimodel_simulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmimodel',
            name='dimensions',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '103x137x37.1')], null=True, verbose_name='Габаритные размеры, ВхШхГ'),
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='humidity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '10%-90% (до 40 ℃); 10%-55% (41-50 ℃)')], null=True, verbose_name='Относительная влажность при эксплуатации'),
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='operating_temp',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '0...+50')], null=True, verbose_name='Рабочая температура, ℃'),
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='storage_temp',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '-20...+60')], null=True, verbose_name='Температура хранения, ℃'),
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='vibration_resistance',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, 'В соответствии с IEC 61131-2')], null=True, verbose_name='Виброустойчивость'),
        ),
        migrations.AddField(
            model_name='hmimodel',
            name='weight',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(30, '280')], null=True, verbose_name='Вес, г'),
        ),
    ]
