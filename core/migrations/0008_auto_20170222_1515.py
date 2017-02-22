# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_useraddon_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddon',
            name='message_channel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraddon',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
