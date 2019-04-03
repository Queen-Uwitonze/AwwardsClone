# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-03 15:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20190403_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]