# Generated by Django 4.0.6 on 2022-09-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0068_alter_series_quick_change_fans'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='automatic_energy_saving',
            field=models.BooleanField(blank=True, null=True, verbose_name='Автоматическое энергосбережение'),
        ),
    ]
