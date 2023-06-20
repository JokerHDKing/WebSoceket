# -*- coding: utf-8 -*-
# @Time    : 2023-02-02 11:31
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : rountings.py
# @Software: PyCharm
from django.urls import re_path

from app01 import consumers
websocket_urlpatterns=[
    #进行路由匹配
    #ws://127.0.0.1:8000/room/群号、
    re_path(r'room/(?P<group>\w+)/$',consumers.ChatConsumer.as_asgi()),
]