# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2020-01-24 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_staffmember_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmember',
            name='name',
            field=models.TextField(default='default'),
        ),
    ]
