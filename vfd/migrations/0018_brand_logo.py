# Generated by Django 4.0.6 on 2022-07-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vfd', '0017_alter_frequencydrive_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ImageField(default=1, upload_to='logos/', verbose_name='Логотип'),
            preserve_default=False,
        ),
    ]
