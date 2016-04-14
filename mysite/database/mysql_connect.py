# -*- coding : utf-8 -*-
__author__ = 'sptty'

import MySQLdb

def mysql_connect(request,user,passwd,db,hosts):
    db = MySQLdb.connect(user=user,passwd=passwd,db=db,hosts=hosts)
    cursor = db.cursor()
    cursor.execute('show tables')
    names = [row[0] for row in cursor.fetchall()]
    print names
    db.close()

