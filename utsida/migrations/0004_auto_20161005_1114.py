# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utsida', '0003_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abroadcourse',
            name='university',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='case',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Language'),
        ),
        migrations.AlterField(
            model_name='case',
            name='university',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='query',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Language'),
        ),
        migrations.AlterField(
            model_name='query',
            name='university',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='University',
        ),
    ]