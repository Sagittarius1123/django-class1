# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import DateTimeField
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateField('创建时间',auto_now=False)
    update_time = models.DateField('更新时间',auto_now=True)
    ownername = models.CharField(max_length=10,null=True)
    coreversion = models.CharField(max_length=30,null=True)
    webversion = models.CharField(max_length=30,null=True)
    remarks = models.CharField(max_length=100,null=True)


    def __unicode__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.CharField(max_length=30,null=True)
    update_time = models.CharField(max_length=30,null=True)
    ownername = models.CharField(max_length=10,null=True)
    coreversion = models.CharField(max_length=30,null=True)
    webversion = models.CharField(max_length=30,null=True)

    def __unicode__(self):
        return self.name
