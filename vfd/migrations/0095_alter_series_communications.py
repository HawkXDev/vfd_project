# Generated by Django 4.0.6 on 2022-09-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0094_alter_series_external_power_24v'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='communications',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (10, 'Плата расширения: Modbus RTU'), (20, 'Платы расширения: Modbus RTU, Profibus DP'), (21, 'Встроен: Modbus RTU'), (30, 'Встроен: Modbus RTU; Платы расширения: DeviceNet, Ethernet IP, Modbus TCP, CANopen, Profibus DP'), (40, 'Встроены: Modbus RTU, BACnet; Платы расширения: DeviceNet, Ethernet IP, Modbus TCP, CANopen, Profibus DP')], null=True, verbose_name='Протоколы связи'),
        ),
    ]
