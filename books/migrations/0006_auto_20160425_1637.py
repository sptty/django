# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 08:37
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160425_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='publication_date',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 4, 25, 16, 37, 46, 349280), null=True),
        ),
    ]
