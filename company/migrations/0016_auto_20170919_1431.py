# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_auto_20170918_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='accountmy_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='accounts_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='admin_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='apps_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='appsdev_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='captcha_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='cms_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='corecli_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='limbo_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='magic_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='mailguy_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='report_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='snapper_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='storage_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='striker_version',
        ),
        migrations.RemoveField(
            model_name='company',
            name='wxservice_version',
        ),
    ]
