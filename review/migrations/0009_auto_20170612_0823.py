# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-12 08:23
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20170612_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='language',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='language',
            name='title_slug',
            field=autoslug.fields.AutoSlugField(default='mandarin', editable=False, populate_from='title', unique=True),
            preserve_default=False,
        ),
    ]
