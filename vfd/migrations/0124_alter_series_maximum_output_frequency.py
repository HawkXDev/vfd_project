# Generated by Django 4.0.6 on 2022-09-21 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0123_alter_series_overload_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='maximum_output_frequency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(10, '320'), (20, '599; 90 кВт и выше: 400'), (30, '599'), (31, '600'), (40, '999'), (50, '3000 (V/F); 300 (SVC)')], null=True, verbose_name='Максимальная выходная частота, Гц'),
        ),
    ]
