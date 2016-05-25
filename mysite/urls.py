# -*- coding:utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


'''
# 老版本的url匹配规则
urlpatterns = patterns('',('^hello/$',hello),
                       ('^time/$',nowtime),
                       ('^books/$',book_list),
                       ('^current_time/$',current_datetime),
                       ('^$',home_page),
                       ('^another-html/$',nowtime),
                       (r'^html/plus/(\d{1,2})/$',offset_time),
                       #  ('^admin$',admin),
                       )

'''

from django.conf.urls.static import *
from django.contrib import admin

from books.models import *
from mysite.database.mysql import *
from mysite.views import *

# from django.conf.urls.defaults import *   # 这是老版本django的导入方法
from django.conf.urls import patterns,include,url  # django 1.9 的方法
admin.autodiscover()


# django1.9  高级url 配置规则
urlpatterns = patterns(
    'mysite.views',
    url('^hello/$','hello',name='hello'),
    url('^time/$','nowtime',name='nowtime'),
    url ('^books/$',books_list),
    url('^current_time/$','current_datetime',name='current_datetime'),
    url('^$','home_page',name='home_page'),
    url('^another-html/$','nowtime',name='nowtime'),
    url(r'^html/plus/(\d{1,2})/$','offset_time',name='offset_time'),
    url('^admin/',include(admin.site.urls)),
    url('^meta$','display_meta',name='display_meta'),
    url('^search-form/$', 'search_form',name='search_form'),
    url('^contact/$', 'contact',name='contact'),
    url('^thanks/$', 'thanks',name='thanks'),
    url(r'article_year/(?P<year>\d{4})/$','article_year',name='article_year'),
    url(r'article_year/$', 'article_year', name='article_year'),
    url(r'article_month/(?P<year>\d{4})/(?P<month>\d{2})/$','article_month',name='article_month'),
    url(r'birthday/(?P<year>\d{4})/(?P<month>\d{2})/$', article_month),
    url(r'^foo/$', foobar, {'template_name': 'html/template_foo.html'}),
    url(r'^bar/$', foobar, {'template_name': 'html/template_bar.html'}),
    url(r'^greet/(?P<greeting>[a-z]*)/(?P<person_name>[a-z]*)/$','greet',name='greet'),
    # url(r'^book/$',book_list),
    # url(r'blog/contact/$',contact_list),
    url(r'^book/$',info_list,{'model':Books}),
    url(r'blog/contact/$', info_list,{'model':Contact}),
    # url(r'^some_page/$','some_page',name='some_page'),
    url(r'^some_page/$', method_splitter,{'GET':some_page_get,'POST':some_page_post}),
)

'''
urlpatterns += patterns(
    'mysite.forms',
    url('^form/', 'Contact_form', name='admin'),
)
'''


# django1.9新版的URL 匹配规则
'''
# django1.9新版的URL 匹配规则
urlpatterns = [
    url('^hello/$',hello),
    url('^time/$',nowtime),
    url ('^books/$',book_list),
    url('^current_time/$',current_datetime),
    url('^$',home_page),
    url('^another-html/$',nowtime),
    url(r'^html/plus/(\d{1,2})/$',offset_time),
    url('^admin/',admin.site.urls),
    url('^meta$',display_meta),
    url('^search-form/$', search_form),
    url('^contact/$', contact),
    url('^thanks/$', thanks),
]
'''


