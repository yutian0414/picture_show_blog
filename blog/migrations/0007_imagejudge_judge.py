# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161020_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagejudge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('judge', models.CharField(max_length=50)),
                ('imageload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.imageload')),
            ],
        ),
        migrations.CreateModel(
            name='judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('judgecomment', models.CharField(max_length=10)),
                ('imageload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.imageload')),
            ],
        ),
    ]
