# Generated by Django 2.2.4 on 2019-09-06 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20190906_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='Старое здание',
            new_name='new_building',
        ),
    ]
