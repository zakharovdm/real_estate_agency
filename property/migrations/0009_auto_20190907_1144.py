# Generated by Django 2.2.4 on 2019-09-07 08:44

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_liked_it'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_it',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
    ]
