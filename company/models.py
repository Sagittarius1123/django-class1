# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=datetime.now)
    update_time = models.DateTimeField(default=datetime.now)
    
class Detail(models.Model):
    name = models.CharField(max_length=30)
    create_time = models.DateTimeField(default=datetime.now)
    account_version = models.CharField(max_length=30)

