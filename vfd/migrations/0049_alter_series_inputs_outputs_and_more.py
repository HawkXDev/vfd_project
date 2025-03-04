# Generated by Django 4.0.6 on 2022-09-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0048_alter_series_control_methods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='inputs_outputs',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'), (2, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'), (3, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2')], null=True, verbose_name='Входы/выходы'),
        ),
        migrations.AlterField(
            model_name='series',
            name='overload_capacity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Лёгкий режим: 120% 60с; \nНормальный режим: 120% 60с, 160% 3с'), (2, '150% 60s; 180% 3s'), (3, 'Нормальный режим: 120% 60с, 150% 3с; \nТяжелый режим: 150% 60с, 200% 3с')], null=True, verbose_name='Перегрузочная способность'),
        ),
    ]
