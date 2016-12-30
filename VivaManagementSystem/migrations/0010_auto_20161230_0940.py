# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-30 04:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VivaManagementSystem', '0009_vms_session_is_current'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='course_id',
            new_name='course',
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set([('course', 'year')]),
        ),
    ]
