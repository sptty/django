# -*- coding:utf-8 -*-
__author__ = 'sptty'

# !/usr/bin/env python

import time

import pika

credentials = pika.PlainCredentials('admin', 'yungui2015')
parameters = pika.ConnectionParameters('172.19.1.3', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    time.sleep( body.count('.') )
    print(" [x] Done")
    #返回消息认证
    ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='task_queue')
channel.start_consuming()