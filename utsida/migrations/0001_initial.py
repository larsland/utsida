# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-30 14:15
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbroadCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('description_url', models.URLField(blank=True, max_length=2000, validators=[django.core.validators.URLValidator])),
                ('study_points', models.FloatField(blank=True, default=7.5)),
                ('pre_requisites', models.ManyToManyField(blank=True, related_name='_abroadcourse_pre_requisites_+', to='utsida.AbroadCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=400)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('D', 'Disapproved')], default='P', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('studyPeriod', models.IntegerField()),
                ('academicQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('socialQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('residentialQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('receptionQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('documentLink', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'continents',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Continent')),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CourseMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('approval_date', models.DateField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('abroadCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.AbroadCourse')),
            ],
            options={
                'verbose_name_plural': 'course matches',
                'verbose_name': 'course match',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('acronym', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'faculties',
            },
        ),
        migrations.CreateModel(
            name='HomeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description_url', models.URLField(blank=True, default='', max_length=2000)),
            ],
            options={
                'verbose_name_plural': 'home courses',
                'verbose_name': 'home course',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('acronym', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=100)),
                ('studyPeriod', models.IntegerField()),
                ('academicQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('socialQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('residentialQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('receptionQualityRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Continent')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Country')),
                ('homeInstitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Institute')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Language')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('acronym', models.CharField(blank=True, max_length=10)),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='utsida.Country')),
            ],
            options={
                'verbose_name_plural': 'universities',
            },
        ),
        migrations.AddField(
            model_name='coursematch',
            name='homeCourse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.HomeCourse'),
        ),
        migrations.AddField(
            model_name='coursematch',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='continent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Continent'),
        ),
        migrations.AddField(
            model_name='case',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Country'),
        ),
        migrations.AddField(
            model_name='case',
            name='homeInstitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Institute'),
        ),
        migrations.AddField(
            model_name='case',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.Language'),
        ),
        migrations.AddField(
            model_name='case',
            name='subjects',
            field=models.ManyToManyField(to='utsida.AbroadCourse'),
        ),
        migrations.AddField(
            model_name='application',
            name='course_matches',
            field=models.ManyToManyField(to='utsida.CourseMatch'),
        ),
        migrations.AddField(
            model_name='application',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.University'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abroadcourse',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utsida.University'),
        ),
        migrations.AlterUniqueTogether(
            name='coursematch',
            unique_together=set([('homeCourse', 'abroadCourse')]),
        ),
        migrations.AlterUniqueTogether(
            name='abroadcourse',
            unique_together=set([('code', 'name', 'university')]),
        ),
    ]
