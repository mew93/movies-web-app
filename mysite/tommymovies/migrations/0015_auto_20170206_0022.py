# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-06 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tommymovies', '0014_auto_20170206_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
