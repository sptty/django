# -*- coding:utf-8 -*-
__author__ = 'sptty'

from django.shortcuts import render_to_response
import MySQLdb

def book_list(request):
    db = MySQLdb.connect(user='sptty',db='db1',passwd='123',host='localhost')
    cursor = db.cursor()
    cursor.execute('show tables')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('html/books.html', {'book_list':names})