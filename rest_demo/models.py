# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class User(models.Model):
    # key是保留字
    username = models.CharField(max_length=255)
    password = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.datetime.now)