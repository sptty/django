# -*- coding:utf-8 -*-
__author__ = 'sptty'

import MySQLdb

from django.shortcuts import render_to_response


def books_list(request):
    db = MySQLdb.connect(user='root',db='django',passwd='root',host='localhost')
    cursor = db.cursor()
    cursor.execute('show tables')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('html/form_books.html', {'books_list':names})
