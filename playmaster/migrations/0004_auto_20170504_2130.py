# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playmaster', '0003_auto_20170504_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='publishedDate',
            new_name='activateDate',
        ),
    ]
