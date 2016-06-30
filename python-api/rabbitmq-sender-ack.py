# -*- coding:utf-8 -*-
__author__ = 'sptty'

#  首先安装 pip install pika

import pika

# import random

credentials = pika.PlainCredentials('admin', 'yungui2015')
#这里可以连接远程IP，请记得打开远程端口
parameters = pika.ConnectionParameters('172.19.1.3',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#channel.queue_declare(queue='hello')
for i in range(1,200):
    # body = 'hello world:%s' %i
    # Queue声明持久化
    channel.queue_declare(queue='task_queue', durable=True)
    message = "Hello World  %s" % i
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=2,)) # 消息声明持久化
    print(" [x] Sent %r" % message)

connection.close()

