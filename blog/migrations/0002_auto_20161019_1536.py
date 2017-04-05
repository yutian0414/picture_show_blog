# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bigsites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigsitesname', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='imageload',
            name='imageurl',
        ),
        migrations.AddField(
            model_name='imageload',
            name='image',
            field=models.ImageField(default='', upload_to='/static/images/'),
        ),
        migrations.AlterField(
            model_name='sites',
            name='siteid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sites',
            name='bigsites',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.bigsites'),
            preserve_default=False,
        ),
    ]
