# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20190403_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='posted_on',
            field=models.DateTimeField(default=True),
        ),
    ]
