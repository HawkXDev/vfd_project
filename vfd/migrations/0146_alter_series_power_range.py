# Generated by Django 4.0.6 on 2022-09-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0145_alter_series_brake_interrupter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='power_range',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...3.7кВт'), (20, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...5.5кВт'), (30, '1x230В: 0.2...2.2кВт; 3x400В: 0.4...7.5кВт'), (40, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...15кВт'), (50, '1x230В: 0.2...2.2кВт; 3x400В: 0.4...22кВт'), (60, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...220кВт'), (61, '1x230В: 0.75...2.2кВт; 3x400В: 0.75...220кВт'), (70, '3x400В: 0.75...500кВт'), (71, '3x400В: 0.75...630кВт'), (72, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...630кВт'), (73, '1x230В: 0.75...2.2кВт; 3x400В: 0.75...630кВт')], null=True, verbose_name='Диапазон мощностей'),
        ),
    ]
