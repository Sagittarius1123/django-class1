# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_auto_20171109_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='create_time',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='update_time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]