# Generated by Django 4.0.6 on 2022-09-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0033_alter_series_power_outages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='additional_communications',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'DeviceNet, Ethernet IP, Modbus TCP, CANopen, Profibus DP')], null=True, verbose_name='Дополнительные протоколы связи'),
        ),
        migrations.AlterField(
            model_name='series',
            name='built_in_communication',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Modbus RTU'), (2, 'Modbus RTU, BACnet')], null=True, verbose_name='Встроенный протокол связи'),
        ),
    ]
