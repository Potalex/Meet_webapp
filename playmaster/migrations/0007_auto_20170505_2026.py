# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-05 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playmaster', '0006_msgpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activateDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
