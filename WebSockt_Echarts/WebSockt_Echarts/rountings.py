# -*- coding: utf-8 -*-
# @Time    : 2023-02-03 10:11
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : rountings.py
# @Software: PyCharm
from django.urls import re_path

from app01 import consumers
websocket_urlpatterns = [
    re_path(r'bar/(?P<group>\w+)/$', consumers.ChatConsumer.as_asgi()),
]