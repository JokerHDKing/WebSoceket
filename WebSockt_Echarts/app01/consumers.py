# -*- coding: utf-8 -*-
# @Time    : 2023-02-03 10:11
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : consumers.py
# @Software: PyCharm
import asyncio
import json
import random
import time

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import  async_to_sync

def randomdata():
    data={"2019":[random.randint(1,i) for i in range(1,28)],
          "2020": [random.randint(1, i) for i in range(1, 28)],
          "2021": [random.randint(1, i) for i in range(1, 28)],
          "2022": [random.randint(1, i) for i in range(1, 28)],
          "生均":[random.randint(1, i) for i in range(1, 28)],
    }
    return data

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 有客户端向后端发送websocket连接请求时，自动触发
        # 服务端允许客户端创建连接
        print("有人来连接了")
        self.accept()
        while True:
            data=randomdata()
            print(data)
            self.send(json.dumps(data))
            #休眠1秒
            time.sleep(1)
        pass

    def websocket_receive(self,message):
        # 浏览器基于websocket向后端发送数据，自动触发接收信息
        # text=webbrowser
        pass

    def websocket_disconnect(self, message):
        # 客户端与服务端断开连接时，自动触发
        print("断开连接")
        raise StopConsumer