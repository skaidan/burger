# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-01-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderelement',
            name='served',
            field=models.BooleanField(default=False),
        ),
    ]