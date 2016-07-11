# -*- encoding:utf-8 -*-
# Create your views here.

from django.shortcuts import render

from models import Article


# 自定义函数
def year_archive(request,year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year':year,'article_list':a_list}
    return render(request,'html/year_archive.html',context)


