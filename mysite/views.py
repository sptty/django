# -*- coding:utf-8 -*-
import MySQLdb
import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


# from django.template import Template, Context
# from django.template.loader import get_template

def hello(request):
	return HttpResponse('hello,world!')


# bad templates
def ua_display_bad(request):
	ua = request.META['HTTP_USER_AGENT']
	return HttpResponse('You browser is %s' % ua)


# good templates one

def ua_display_good1(request):
	try:
		ua = request.META['HTTP_USER_AGENT']
	except KeyError:
		ua = 'unknown'
	return HttpResponse('You are browser is %s'% ua)


# good templates two

def ua_display_good2(request):
	ua = request.META.get('HTTP_USER_AGENT','unknown')
	return HttpResponse('You are browser is %s ' % ua)


def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('html/current_date.html', {'current_date':now})


def display_meta(request):
    vaules = request.META.items()
    vaules.sort()
    html = []
    for k,v in vaules:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
        # html.append('\n')
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render_to_response('html/meta_info.html',{'meta_all_info':'\n'.join(html)})

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
    print(sum_row)
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

'''def search_form(request):
    return render_to_response('html/form_search.html')
'''

from books.models import Books

def search_form(request):
    errors = []
    # error_len = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please submit a Search term.')
        elif len(q) > 10:
            errors.append('Sorry again , a Search term must  length less than 10')
        else:
            books = Books.objects.filter(title__icontains=q)
            return render_to_response('html/form_search_result.html',{'query':q,'books':books})
    return render_to_response('html/form_search.html', {'errors':errors})


from books.models import Contact

# 将提交的表单信息写入数据库
def contact_table(results):
    contact_info = Contact(subject=results[0],telephone=results[1],email=results[2],message=results[3])
    contact_info.save()
    '''Contact.subject = results[0]
    Contact.email = results[1]
    Contact.telephone = results[2]
    Contact.message = results[3]
    Contact.save()'''


def contact(request):
    errors = []
    results = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        if not request.POST.get('telephone',''):
            errors.append('Enter a telephone')
        elif len(request.POST.get('telephone','')) != 11:
            errors.append('请输入11位电话号码')
            # errors.append(len(request.POST.get('telephone','')))
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            '''
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email','noreply@example.com'),
                ['wanhb_yg@yun-gui.com'],
            )
            '''
            results.append(request.POST['subject'])
            results.append(request.POST['telephone'])
            results.append(request.POST['email'])
            results.append(request.POST['message'])
            contact_table(results)  # 调用函数,将数据写入数据库
            # return HttpResponseRedirect('/html/thanks.html')
            # return render_to_response('html/form_contact.html',{'infos':results})

            return HttpResponseRedirect('/thanks/')
    return render_to_response('html/form_contact.html',
                                  {'errors':errors,
                              'subject': request.POST.get('subject',''),
                              'message':request.POST.get('message',''),
                              'telephone':request.POST.get('telephone',''),
                              'email':request.POST.get('email',''),
                                   })


def thanks(request):
    return render_to_response('html/thanks.html')



