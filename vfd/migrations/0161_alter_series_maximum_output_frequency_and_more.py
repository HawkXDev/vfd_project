# Generated by Django 4.0.6 on 2022-09-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0160_alter_series_power_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='maximum_output_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '320'), (20, '599; 90 кВт и выше: 400'), (21, '500'), (22, '400'), (30, '599'), (31, '600'), (40, '999'), (50, '3000 (V/F); 300 (SVC)'), (51, '3200 (V/F); 300 (SVC)'), (52, '3200 (V/F); 500 (SVC)'), (53, '5000')], null=True, verbose_name='Максимальная выходная частота, Гц'),
        ),
        migrations.AlterField(
            model_name='series',
            name='starting_torque',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '150% / 0.5 Гц'), (11, 'G type: 150% / 0.5 Гц (SVC)'), (12, 'G type: 150% / 0.5 Гц (SVC);\nP type: 100% / 0.5 Гц'), (13, '150% / 3 Гц (V/F), \n150% / 1 Гц (FVC)'), (14, '150% / 3 Гц (V/F, SVC для IM в тяжёлом режиме)\n100% / 2.5 Гц (V/F, SVC для PM в тяжёлом режиме)'), (15, '100% / 0.5 Гц (V/F); 150% / 0.5 Гц (SVC)'), (16, '150% / 3(1) Гц (V/F); 150% / 0.5 Гц (SVC)'), (17, 'G type: 150% / 0.5 Гц; \nP type: 100% / 0.5 Гц'), (18, 'Auto torque boost, manual torque boost 0.1%-30%; Vector torque boost 100-150; Start frequency 0.4Hz-20Hz'), (19, '150% / 0.25 Гц (SVC)'), (20, 'G type: 150% / 0.5 Гц (SVC), 180% / 0 Гц (VC);\nP type: 100% / 0.5 Гц'), (21, 'Auto torque boost, manual torque boost 0.1%-30%; Cut-off frequency of torque boost 0Hz to maximum output frequency')], null=True, verbose_name='Пусковой момент'),
        ),
    ]
