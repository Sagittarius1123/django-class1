# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20170918_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='remark',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
