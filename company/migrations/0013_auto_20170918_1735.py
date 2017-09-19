# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20170917_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='accountmy_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='accounts_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='admin_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='apps_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='appsdev_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='captcha_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='cms_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='core_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='corecli_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='limbo_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='magic_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='mailguy_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='owner',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='report_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='snapper_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='storage_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='striker_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='web_version',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='wxservice_version',
            field=models.CharField(max_length=30, null=True),
        ),
    ]