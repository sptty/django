# -*- coding:utf-8 -*-
import datetime

from django.http import HttpResponse
# from django.template import Template, Context
# from django.template.loader import get_template
from django.shortcuts import render_to_response
import MySQLdb


def hello(request):
	return HttpResponse('hello,world!')


def nowtime(request):
	now = datetime.datetime.now()	
	html = "<html><body> It is now %s.</body></html>" % now
	return HttpResponse(html)


def home_page(request):
	return HttpResponse('this is home page!')

'''
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s .</body></html>" % now
	return HttpResponse(html)


def current_datetime(request):
	now = datetime.datetime.now()
	person = {'name':'sptty'}
	t = Template('<html><body>It is now {{ current_date }} , My name is {{ person.name }}.</body></html>')
	html = t.render(Context({'current_time':now},{'person':person}))
	return HttpResponse(html)


def current_datetime(request):
	now = datetime.datetime.now()
	person = {'person':'sptty'}
	t = get_template('current_date.html')
	html = t.render(Context({'current_date':now}))
	return HttpResponse(html)
'''


def books(request):
	connections = MySQLdb.connect(user='sptty',passwd='123',db='db1')
	cursor = connections.cursor()
	cursor.execute("show tables")
	sum_row = cursor.fetchall()
	print sum_row
	return render_to_response('html/books.html', {'books_row':str(sum_row)})


'''
def current_datetime(request):
	now = datetime.datetime.now()
	person = {'name':'Sptty', 'current_date':str(now)}
	return render_to_response('current_date.html',{'person':person})


def current_datetime(request):
	now = datetime.datetime.now()
	person = {'name':'Sptty.wan','current_date':now}
	t = get_template('html/current_date.html')
	return render_to_response('html/current_date.html',{'person':now})
	# return render_to_response(t.origin,{'person':person})




def current_datetime(request):
	now = datetime.datetime.now()
	# person = {'name':'张玉','current_date':now}
	return render_to_response('html/current_date.html',{'current_date':now})
'''

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('html/current_date.html', {'current_date':now})


def offset_time(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise ArithmeticError
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# assert False
	# html = "<html><body>In %s hour(s).it will be %s.</body></html>" % (offset, dt)
	plus = {'hour_offset':offset,'next_time':dt}
	return render_to_response('html/plus_hours.html', {'plus':plus})



