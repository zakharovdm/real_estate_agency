# Generated by Django 2.2.4 on 2019-09-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_новостройка'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='Новостройка',
        ),
        migrations.AddField(
            model_name='flat',
            name='Старое здание',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),
    ]
