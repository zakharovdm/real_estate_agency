# Generated by Django 2.2.4 on 2019-09-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20190908_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца:'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owner_flats',
            field=models.ManyToManyField(db_index=True, related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности:'),
        ),
    ]
