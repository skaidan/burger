# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-01-26 19:59
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0007_auto_20200126_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
