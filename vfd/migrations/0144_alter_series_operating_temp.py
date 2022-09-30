# Generated by Django 4.0.6 on 2022-09-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0143_alter_series_overload_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='operating_temp',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '-10...+40'), (20, '-10...+40; \nСо снижением характеристик -10...+50'), (21, '-10...+40(50)'), (30, '-10...+40(50); \nСо снижением характеристик -10...+60'), (50, '-20...+50; \nСо снижением характеристик -20...+60')], null=True, verbose_name='Рабочая температура, ℃'),
        ),
    ]
