# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20170611_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='pronunciation',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
