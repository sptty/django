# -*- coding:utf-8 -*-
import MySQLdb
import datetime

from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.shortcuts import render_to_response

from books.models import Books
from mysite.forms import Contact_form


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
    return render_to_response('html/form_books.html', {'books_row':str(sum_row)})


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
def contact_table(**results):
    contact_info = Contact(subject=results['subject'],
                           telephone=results['telephone'],
                           email=results['email'],
                           message=results['message']
                           )
    contact_info.save()

    '''Contact.subject = results[0]
    Contact.email = results[1]
    Contact.telephone = results[2]
    Contact.message = results[3]
    Contact.save()'''

"""
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
"""


def contact(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            contact_table(**form_data)
            return HttpResponseRedirect('/thanks/')
    else:       # 第一次访问直接到这里
        form = Contact_form(initial={'subject':'请输入邮件主题'})
    return render_to_response('html/form_contact.html',{'form':form})


def thanks(request):
    return render_to_response('html/thanks.html')


def article_year(request,year='2015'):
    return HttpResponse(str(year+' year.'))


def article_month(request,year,month):
    try:
        title = str(year + ' year ' + month + ' month.')
    except ValueError:
        return HttpResponse('month is not right!')
    return HttpResponse(title)


def foobar(request,template_name):
    return render_to_response(template_name=template_name)


def greet(request,person_name,greeting):
    greeting = greeting
    person_name = person_name
    return HttpResponse(str(greeting+' ' +person_name))

'''
def book_list(request):
    obj_list = Books.objects.all()
    return render_to_response('html/form_books.html', {'books_list':obj_list})


def contact_list(request):
    obj_list = Contact.objects.all()
    return render_to_response('html/form_contact.html',{'contact_list':obj_list})

'''

def info_list(request,model):
    obj_list = model.objects.all()
    obj_list = str(obj_list)
    return render_to_response('html/form_%s.html' % model.__name__.lower(),{'object_list':obj_list})


def method_splitter(request,*args,**kwargs):
    get_view = kwargs.pop('GET',None)
    post_view = kwargs.pop('POST',None)
    if request.method == 'POST' and post_view is not None:
        return HttpResponseRedirect('/thanks/')
    elif request.method == 'GET' and get_view is not None:
        return render_to_response('html/form_books.html')
    else:
        raise Http404


def some_page_get(request,*args,**kwargs):
    assert request.method == 'GET'
    return render_to_response('html/form_books.html')


def some_page_post(request):
    assert request.method == 'POST'
    return HttpResponseRedirect('/thanks/')


def some_page(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/thanks/')      # 注意HttpResponseRedirect参数写的是URL
    elif request.method == 'GET':
        return render_to_response('html/form_books.html')
    else:
        raise Http404

