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
from django.conf.urls import *
from django.contrib import admin

from mysite.database.mysql import *
from mysite.views import *

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


# django1.9新版的URL 匹配规则

admin.autodiscover()

urlpatterns = [
    url('^hello/$',hello),
    url('^time/$',nowtime),
    url ('^books/$',book_list),
    url('^current_time/$',current_datetime),
    url('^$',home_page),
    url('^another-html/$',nowtime),
    url(r'^html/plus/(\d{1,2})/$',offset_time),
    url('^admin/',admin.site.urls),
    ]