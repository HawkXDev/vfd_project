# Generated by Django 4.0.6 on 2022-09-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0006_alter_country_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Название'),
        ),
    ]
