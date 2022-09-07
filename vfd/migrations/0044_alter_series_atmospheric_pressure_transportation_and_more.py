# Generated by Django 4.0.6 on 2022-09-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0043_series_atmospheric_pressure_transportation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='atmospheric_pressure_transportation',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Атмосферное давление при транспортировке, кПа'),
        ),
        migrations.AlterField(
            model_name='series',
            name='atmospheric_pressure_use_storage',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Атмосферное давление при эксплуатации/хранении, кПа'),
        ),
        migrations.AlterField(
            model_name='series',
            name='operating_temp',
            field=models.CharField(blank=True, choices=[('-10...+40', '-10...+40'), ('-10...+50', '-10...+50'), ('-15...+50', '-15...+50'), ('-20...+50', '-20...+50'), ('-25...+70', '-25...+70')], max_length=200, null=True, verbose_name='Рабочая температура, ℃'),
        ),
        migrations.AlterField(
            model_name='series',
            name='storage_temp',
            field=models.CharField(blank=True, choices=[('-10...+40', '-10...+40'), ('-10...+50', '-10...+50'), ('-15...+50', '-15...+50'), ('-20...+50', '-20...+50'), ('-25...+70', '-25...+70')], max_length=200, null=True, verbose_name='Температура хранения, ℃'),
        ),
        migrations.AlterField(
            model_name='series',
            name='transport_temp',
            field=models.CharField(blank=True, choices=[('-10...+40', '-10...+40'), ('-10...+50', '-10...+50'), ('-15...+50', '-15...+50'), ('-20...+50', '-20...+50'), ('-25...+70', '-25...+70')], max_length=200, null=True, verbose_name='Температура транспортировки, ℃'),
        ),
        migrations.AlterField(
            model_name='series',
            name='vibration',
            field=models.TextField(blank=True, null=True, verbose_name='Вибрация'),
        ),
    ]
