# Generated by Django 4.0.6 on 2022-09-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='EquipmentLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Линейка оборудования',
                'verbose_name_plural': 'Линейки оборудования',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
                ('site', models.CharField(max_length=150, verbose_name='Сайт')),
                ('currency', models.CharField(choices=[('BYN', 'BYN'), ('RUB', 'RUB'), ('EUR', 'EUR'), ('USD', 'USD')], max_length=200, verbose_name='Валюта')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('site', models.CharField(max_length=150, verbose_name='Сайт')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logos/', verbose_name='Логотип')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.country', verbose_name='Страна')),
                ('equipment_lines', models.ManyToManyField(to='supplier.equipmentline', verbose_name='Линейки оборудования')),
                ('suppliers', models.ManyToManyField(to='supplier.supplier', verbose_name='Поставщики')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
    ]
