# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utsida', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='continent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='utsida.Continent'),
        ),
        migrations.AddField(
            model_name='query',
            name='continent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='utsida.Continent'),
        ),
    ]