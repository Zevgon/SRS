# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_word_times_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='know_status',
            field=models.IntegerField(default=0),
        ),
    ]
