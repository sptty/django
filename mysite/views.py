# -*- coding:utf-8 -*-
import MySQLdb
import datetime

from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.shortcuts import render_to_response

from books.models import Books
from mysite.forms import Contact_form


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


# 包装视图函数
def requires_login(view):
    def new_view(request,*args,**kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/thanks/')
        return view(request,*args,**kwargs)
    return new_view


# 下为第九章相关笔记
'''

def view_1(request):
    t = loader.get_template('html/thanks.html')
    c = Context({
        'app':'My app',
        'user':request.user,
        'ip_address':request.META['REMOTE_ADDR'],
        'message':'I am the first view.',
    })
    return t.render(c)

def view_2(request):
    t = loader.get_template('html/form_books.html')
    c = Context({
        'app':'My app',
        'user':request.user,
        'ip_address':request.META['REMOTE_ADDR'],
        'message':'I am the second view.',
    })
    return t.render(c)

def view_1(request):
    t = loader.get_template('html/tag_context.html')
    c = RequestContext(
        request,
        {'message':'I am  view 1.',},
        processors=[custom_proc],   # context处理器
    )
    return HttpResponse(t.render(c))


def view_2(request):
    t = loader.get_template('html/tag_context.html')
    c = RequestContext(
        request,
        {'message':'I am a second view'},
        processors=[custom_proc],       # context处理器
    )
    return  HttpResponse(t.render(c))



# 定义context处理器,接受http request请求然后返回一个字典,字典包含可以在模板context中使用的变量
def custom_proc(request):
    __doc__ = '定义context处理器,接受http request请求然后返回一个字典,字典包含可以在模板context中使用的变量'
    "A Context processor that provides 'app','user','ip_address'."
    return {
        'app':'My app',
        'user':request.user,
        'ip_address':request.META['REMOTE_ADDR']
    }


def view_1(request):
    return render_to_response(
        'html/tag_context.html',
        {'message':'I am a view one'},
        context_instance=RequestContext(request,processors=[custom_proc])
                              )


def view_2(request):
    return render_to_response(
        'html/tag_context.html',
        {'message':"I am the view two ."},
        context_instance=RequestContext(request,processors=[custom_proc]),
                              )


def view_3(request):
    return render_to_response(
        'html/tag_context.html',
        {'message':'I am the view three.'},
        context_instance=RequestContext(request,processors=[custom_proc]),
    )


def view_4(request):
    return render_to_response(
        'html/tag_context.html',
        {'message':"<script>alert('^_^ 哈哈哈 这是个玩笑,张玉就是个250 阿  ^_^哈啊华^_^!')</script>",},
        # 通过这段html代码,且模板中{{message|safe}} 不转意特殊字符,那么在web访问的时候 将执行这段代码,效果就是弹出小窗口
        context_instance=RequestContext(request,processors=[custom_proc]),
    )


def view_5(request):
    return render_to_response(
        'html/tag_context.html',
        {'message':"I am <b>the view five."},
        context_instance=RequestContext(request,processors=[custom_proc]),
    )

def view_6(request):
    t = loader.get_template('html/tag_context.html')
    c = RequestContext(
        request,
        {'message':'This is the view six!!!'},
        processors=[custom_proc],
    )


def tag_books(request):
    t = loader.get_template('html/tag_books.html')
    c = RequestContext(request)
    return t.render(c)
'''

def tag_books(request):
    # books = str(books)
    return render_to_response('html/tag_books.html')