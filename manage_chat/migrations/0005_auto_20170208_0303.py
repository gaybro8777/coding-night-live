# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import manage_chat.models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_chat', '0004_chatandreply_assist_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatandreply',
            name='assist_hash',
            field=models.CharField(default=0, max_length=7),
        ),
        migrations.AlterField(
            model_name='chatandreply',
            name='hash_value',
            field=models.CharField(default=manage_chat.models._createHash, max_length=7, unique=True),
        ),
    ]
