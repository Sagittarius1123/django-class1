# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import DateTimeField
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateField('创建时间',auto_now=False)
    update_time = models.DateField('更新时间',auto_now=True)

    def __unicode__(self):
        return self.name

class Detail(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    account_version = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name
