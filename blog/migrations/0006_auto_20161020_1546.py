# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161020_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageload',
            name='image',
            field=models.ImageField(default='', upload_to='./uploads/'),
        ),
    ]
