# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-22 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tommymovies', '0002_auto_20170122_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='watch_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Watched'),
        ),
    ]
