# -*- coding:utf-8 -*-
__author__ = 'sptty'

# !/usr/bin/env python

import pika

credentials = pika.PlainCredentials('admin', 'yungui2015')
parameters = pika.ConnectionParameters('172.19.1.3', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    # time.sleep(0.2)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()