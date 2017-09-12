# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import DateTimeField
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    
class Detail(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    account_version = models.CharField(max_length=30)

