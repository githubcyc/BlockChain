# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets, serializers
# from .serializers import UserSerializer
from .models import User
# Create your views here.
# https://www.cnblogs.com/jonathan1314/p/7154243.html#2000

# Serializers定义了API的表现.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'create_time')

# ViewSets 定义了 视图（view）的行为
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer