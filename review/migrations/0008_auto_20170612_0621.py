# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 06:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_word_know_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='bucket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='review.Bucket'),
        ),
    ]