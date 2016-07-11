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


# 定义作者sptty的管理类

class XinBookMnanger(models.Manager):
    def get_query_set(self):
        return super(XinBookMnanger,self).get_query_set().filter(author='wan hongbow')

# 定义书籍的manger方法

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()    # title__icontains 注意这里是两个下划线!!

    def author_list(self):
        author_list_all = []
        for i in Books.objects.all():
            author_list_all.append(i)
        return author_list_all

# 定义类:书籍信息

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null=True)
    objects = BookManager()
    xin_objects = XinBookMnanger()

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


# 测试create table
class Ctest(models.Model):
    colume1 = models.CharField(max_length=10)
    colume2 = models.CharField(max_length=20)
    colume3 = models.CharField(max_length=30)

    def __unicode__(self):
        return self.colume1

    class Meta:
        ordering = ['colume1']


# 定义书籍的manger方法

class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title_icontains=keyword).count()



# 测试create table
class Ctest(models.Model):
    colume1 = models.CharField(max_length=10)
    colume2 = models.CharField(max_length=20)

    def __unicode__(self):
        return self.colume1

    class Meta:
        ordering = ['colume1']


# 定义管理类

class MaleManager(models.Manager):
    def get_query_set(self):
        return super(MaleManager,self).get_query_set().filter(sex='M')

class FemaleManager(models.Manager):
    def get_query_set(self):
        return super(FemaleManager, self)


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1,choices=(('M','Male'),('F','Female')))
    # birth_date = models.DateField()
    # address = models.CharField(max_length=100)
    # city = models.CharField(max_length=50)
    # state = models.CharField(max_length=30)
    men = MaleManager()
    women = FemaleManager()


# django 1.8
class Reporter(models.Model):
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter)

    def __str__(self):
        return self.headline
