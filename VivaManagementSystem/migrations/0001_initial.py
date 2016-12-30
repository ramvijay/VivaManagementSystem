# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-15 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'Batch',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=10)),
                ('core_competency', models.CharField(max_length=30)),
                ('areas_of_interest', models.TextField()),
                ('phone_number', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('semester', models.IntegerField(choices=[(7, '7'), (9, '9'), (4, '4')])),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('project_category', models.CharField(choices=[('Industry', 'Industry Project'), ('Research', 'Institution/Research Project')], max_length=20)),
                ('organization_name', models.CharField(max_length=200)),
                ('postal_address', models.CharField(max_length=500)),
                ('address_short_url', models.CharField(max_length=200)),
                ('mentor_name', models.CharField(max_length=100)),
                ('mentor_designation', models.CharField(max_length=100)),
                ('domain_key_word', models.CharField(max_length=300)),
                ('project_title', models.CharField(max_length=500)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VivaManagementSystem.Course')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='VivaManagementSystem.Course'),
        ),
        migrations.AddField(
            model_name='batch',
            name='tutor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VivaManagementSystem.Faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set([('course_id', 'year')]),
        ),
    ]