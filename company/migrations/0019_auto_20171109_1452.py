# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_auto_20170919_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('create_time', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('ownername', models.CharField(max_length=10, null=True)),
                ('coreversion', models.CharField(max_length=30, null=True)),
                ('webversion', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
    ]
