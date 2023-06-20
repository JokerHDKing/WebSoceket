# -*- coding: utf-8 -*-
# @Time    : 2023-02-02 11:35
# @Author  : Huang Deng
# @Email   : 280418304@qq.com
# @File    : consumers.py
# @Software: PyCharm
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import  StopConsumer
from asgiref.sync import  async_to_sync

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print("有人来连接了")
        #有客户端向后端发送websocket连接请求时，自动触发
        #服务端允许客户端创建连接（握手。）
        self.accept()
        #获取群号，获取路由匹配中的群号
        group=self.scope['url_route']['kwargs'].get('group')
        #将客户端的连接对象加入到某个地方（内存 或者 redis）===>async_to_sync：将异步的功能转换为同步的功能
        async_to_sync(self.channel_layer.group_add) (group,self.channel_name)


        pass
    def websocket_receive(self, message):
        group=self.scope['url_route']['kwargs'].get('group')

        #通知组内的所有客户端、执行xx_oo方法，在此方法中自己可以去定义任意的功能
        async_to_sync(self.channel_layer.group_send)(group,{"type":"xx.oo",'message':message})
        pass
    def xx_oo(self,event):
        text=event['message']['text']
        self.send(text)
    def websocket_disconnect(self, message):
        group=self.scope['url_route']['kwargs'].get('group')
        #客户端与服务端断开连接时，自动触发
        async_to_sync(self.channel_layer.group_discard)(group,self.channel_name)
        print("断开连接")
        raise StopConsumer