# Generated by Django 2.2.4 on 2019-09-06 18:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0007_auto_20190906_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_it',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
    ]
