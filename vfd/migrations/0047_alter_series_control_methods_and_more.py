# Generated by Django 4.0.6 on 2022-09-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0046_alter_series_copy_backup_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='control_methods',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(2, 'V/F (скалярное управление), \nSVC (бездатчиковое векторное управление)')], null=True, verbose_name='Методы управления'),
        ),
        migrations.AlterField(
            model_name='series',
            name='motor_cable_length',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Без дросселя: экран.кабель 35...100м в зависимости от номинала; неэкран. 50...150м. \nС дросселем: экран.кабель 50...150м; неэкран. 90...225м'), (2, 'Без дросселя: экран.кабель 50...150м в зависимости от номинала; неэкран. 75...225м. \nС дросселем: экран.кабель 75...225м; неэкран. 115...325м')], null=True, verbose_name='Максимальная длина кабеля двигателя'),
        ),
        migrations.AlterField(
            model_name='series',
            name='operating_temp',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '-10...+40(+50); \nСо снижением характеристик -10...+60'), (2, '-20...+50; \nСо снижением характеристик -20...+60')], null=True, verbose_name='Рабочая температура, ℃'),
        ),
        migrations.AlterField(
            model_name='series',
            name='overload_capacity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Лёгкий режим: 120% 60с; \nНормальный режим: 120% 60с, 160% 3с'), (2, 'Нормальный режим: 120% 60с, 150% 3с; \nТяжелый режим: 150% 60с, 200% 3с')], null=True, verbose_name='Перегрузочная способность'),
        ),
        migrations.AlterField(
            model_name='series',
            name='power_range',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, '1x220В: 0.4...2.2кВт; 3x380В: 0.75...3.7кВт'), (2, '1x220В: 0.2...2.2кВт; 3x380В: 0.4...22кВт'), (3, '0.75...500кВт')], null=True, verbose_name='Диапазон мощностей'),
        ),
        migrations.AlterField(
            model_name='series',
            name='wall_to_wall_installation',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Допускается для ПЧ от 45 кВт включительно; \nДо 45 кВт: зазор 10мм'), (2, 'Допускается при макс.окруж.темп. до -40℃, \nдо -50℃ со снижением характеристик')], null=True, verbose_name='Монтаж "Стенка к стенке"'),
        ),
    ]
