# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_company_remark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='owner',
            new_name='ownername',
        ),
    ]