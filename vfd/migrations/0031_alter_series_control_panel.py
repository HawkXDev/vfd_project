# Generated by Django 4.0.6 on 2022-09-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0030_series_control_panel_desc_alter_series_control_panel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='control_panel',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Светодиодная 4-символьная'), (2, 'Светодиодная 5-символьная'), (3, 'ЖК-дисплей')], null=True, verbose_name='Панель управления'),
        ),
    ]
