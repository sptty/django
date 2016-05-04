# -*- coding:utf-8 -*-
__author__ = 'sptty'

#  首先安装 pip install pika

import time

import pika

# import random


credentials = pika.PlainCredentials('admin', 'yungui2015')
#这里可以连接远程IP，请记得打开远程端口
parameters = pika.ConnectionParameters('172.19.1.3',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#channel.queue_declare(queue='hello')
for i in range(1,20000):
    body = 'hello world:%s' %i
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=body)
    print(" [x] Sent %s" %body)
    time.sleep(0.2)

connection.close()

