# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20161117_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_courses',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
    ]
