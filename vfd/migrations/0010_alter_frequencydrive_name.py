# Generated by Django 4.0.6 on 2022-07-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0009_alter_application_name_alter_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencydrive',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Наименование'),
        ),
    ]
