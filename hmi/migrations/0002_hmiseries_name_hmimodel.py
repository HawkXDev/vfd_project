# Generated by Django 4.0.6 on 2022-12-13 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hmiseries',
            name='name',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HmiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=20, unique=True, verbose_name='Артикул')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hmi.hmiseries', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Серия',
                'verbose_name_plural': 'Серии',
            },
        ),
    ]
