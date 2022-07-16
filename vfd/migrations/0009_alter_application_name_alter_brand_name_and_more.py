# Generated by Django 4.0.6 on 2022-07-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0008_alter_series_additional_communications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='equipmentline',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='series',
            name='built_in_plc',
            field=models.CharField(choices=[('No', 'Нет')], max_length=200, verbose_name='Встроенный ПЛК'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='series',
            name='operating_temp',
            field=models.CharField(choices=[('-10...+50', '-10...+50'), ('-15...+50', '-15...+50')], max_length=200, verbose_name='Рабочая температура'),
        ),
        migrations.AlterField(
            model_name='series',
            name='protection_degree',
            field=models.CharField(choices=[('IP20', 'IP20'), ('IP21', 'IP21'), ('IP55', 'IP55'), ('IP20/IP55', 'IP20/IP55'), ('IP21/IP55', 'IP21/IP55')], max_length=200, verbose_name='Степень защиты'),
        ),
    ]
