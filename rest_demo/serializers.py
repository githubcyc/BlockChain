from django.db import models
import datetime


class UserSerializer(models.Model):
    # key是保留字
    username = models.CharField(max_length=255)
    password = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.datetime.now)