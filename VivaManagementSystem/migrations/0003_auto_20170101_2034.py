# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-01 15:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VMS', '0002_auto_20170101_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('user', 'user_role')]),
        ),
    ]