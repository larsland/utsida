# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-29 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utsida', '0002_auto_20161129_0955'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='saved_course_matches',
            field=models.ManyToManyField(to='utsida.CourseMatch'),
        ),
    ]