# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-06 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utsida', '0003_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_match_application',
            name='status',
        ),
        migrations.AddField(
            model_name='course_match_application',
            name='shirt_size',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Disapproved')], default='P', max_length=2),
        ),
    ]