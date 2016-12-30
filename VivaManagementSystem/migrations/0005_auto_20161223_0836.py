# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-23 03:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VivaManagementSystem', '0004_auto_20161223_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='Course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='tutor',
            old_name='empId',
            new_name='faculty',
        ),
        migrations.AlterUniqueTogether(
            name='tutor',
            unique_together=set([('session', 'faculty', 'course')]),
        ),
    ]