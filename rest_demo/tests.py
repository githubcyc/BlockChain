# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

import json
import requests
from urllib.parse import urljoin
 
BASE_URL = 'http://127.0.0.1:8000/'
AUTH = ('admin', 'django123')
 
def test_get_user_list():
    rsp = requests.get(urljoin(BASE_URL, '/rest_demo/users/'), auth=AUTH, headers={
        'Accept': 'application/json'
    })
    print(rsp.text)
    assert rsp.ok
 
def test_post_user_list():
    json_data = dict(
        password=0,
        nick='oo',
        create_time='2014-03-3T03:3:3'
    )
    rsp = requests.post(urljoin(BASE_URL, '/rest_demo/users/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, data=json.dumps(json_data))
    print(rsp.text)
    assert(rsp.ok)
 
def test_get_user():
    rsp = requests.get(urljoin(BASE_URL, '/rest_demo/users/1'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    })
    assert rsp.ok
 
def test_put_user():
    json_data = dict(
        password=100,
        nick='xx',
        create_time='2014-03-3T03:3:3'
    )
    # 注意最后的 /
    rsp = requests.put(urljoin(BASE_URL, '/rest_demo/users/1/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
    )
    assert rsp.ok, rsp.status_code
 
def test_patch_user():
    json_data = dict(
        password=300,
        )
    rsp = requests.patch(urljoin(BASE_URL, '/rest_demo/users/1/'), auth=AUTH, headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }, data=json.dumps(json_data),
    )
    print(rsp.text)
    assert rsp.ok, rsp.status_code


if __name__ == '__main__':
    test_patch_user()