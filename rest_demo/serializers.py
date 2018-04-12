from django.db import models
import datetime


class UserSerializer(models.Model):
    # key是保留字
    password = models.IntegerField()
    nick = models.CharField(max_length=255)
    create_time = models.DateTimeField(default=datetime.datetime.now)