# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-28 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VivaManagementSystem', '0007_auto_20161228_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='short_name',
            field=models.CharField(default='none', max_length=5),
        ),
    ]
