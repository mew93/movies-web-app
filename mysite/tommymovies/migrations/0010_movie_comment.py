# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tommymovies', '0009_auto_20170202_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
