# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170222_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddon',
            name='token',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
