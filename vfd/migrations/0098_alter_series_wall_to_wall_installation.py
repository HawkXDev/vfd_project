# Generated by Django 4.0.6 on 2022-09-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0097_alter_series_pre_configurations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='wall_to_wall_installation',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Нет'), (1, 'Допускается для ПЧ от 45 кВт включительно; \nДо 45 кВт: зазор 10мм'), (2, 'Допускается при макс.окруж.темп. до -40℃, \nдо -50℃ со снижением характеристик')], null=True, verbose_name='Монтаж "Стенка к стенке"'),
        ),
    ]
