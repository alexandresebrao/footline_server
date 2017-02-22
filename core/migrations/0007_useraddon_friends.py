# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20170222_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddon',
            name='friends',
            field=models.ManyToManyField(related_name='Friends', to=settings.AUTH_USER_MODEL),
        ),
    ]