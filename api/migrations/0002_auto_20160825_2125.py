# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssitem',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rssitem',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
