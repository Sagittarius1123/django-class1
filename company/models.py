# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import DateTimeField
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateField('创建时间',auto_now=False)
    update_time = models.DateField('更新时间',auto_now=True)
    owner = models.CharField(max_length=10,null=True)
    accounts_version = models.CharField(max_length=30,null=True)
    accountmy_version = models.CharField(max_length=30,null=True)
    apps_version = models.CharField(max_length=30,null=True)
    appsdev_version = models.CharField(max_length=30,null=True)
    captcha_version = models.CharField(max_length=30,null=True)
    core_version = models.CharField(max_length=30,null=True)
    limbo_version = models.CharField(max_length=30,null=True)
    magic_version = models.CharField(max_length=30,null=True)
    mailguy_version = models.CharField(max_length=30,null=True)
    cms_version = models.CharField(max_length=30,null=True)
    admin_version = models.CharField(max_length=30,null=True)
    snapper_version = models.CharField(max_length=30,null=True)
    storage_version = models.CharField(max_length=30,null=True)
    corecli_version = models.CharField(max_length=30,null=True)
    striker_version = models.CharField(max_length=30,null=True)
    web_version = models.CharField(max_length=30,null=True)
    wxservice_version = models.CharField(max_length=30,null=True)
    report_version = models.CharField(max_length=30,null=True)
    remark = models.CharField(max_length=100,null=True)

    
    def __unicode__(self):
        return self.name

class Detail(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    account_version = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
