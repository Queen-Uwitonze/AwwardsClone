# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-01 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20190401_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='score',
        ),
        migrations.RemoveField(
            model_name='project',
            name='vote',
        ),
    ]
