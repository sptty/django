# -*- coding:UTF-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

'''
此处都是跟数据库相关的信息:
定义以下的类,然后在项目路径下面执行:
注意：Django 1.7 及以上的版本需要用以下命令
    python manage.py makemigrations
    python manage.py migrate
然后查看数据库即可看到已经建立了相应的表格:

mysql> show tables;
+-----------------------------------+
| Tables_in_db1                     |
+-----------------------------------+
| books_author                      |
| books_books                       |
| books_books_author                |
| books_publisher


'''

# 定义类:出版社信息

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


# 定义类:作者信息

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True,verbose_name='e-mail')

    def __unicode__(self):
        return '%s %s' % (self.first_name,self.last_name)


# 定义类:书籍信息

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null=True)

    def __unicode__(self):
        return self.title

# 定义类:联系人信息

class Contact(models.Model):
    subject = models.CharField(max_length=50)
    email = models.EmailField(blank=True,verbose_name='e-mail')
    telephone = models.BigIntegerField()
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.subject