# Generated by Django 4.0.6 on 2022-09-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0008_alter_series_emc_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='applications',
            field=models.ManyToManyField(blank=True, null=True, to='vfd.application', verbose_name='Применения'),
        ),
    ]
