# -*- coding:utf-8 -*-
from django import template

from books.models import Books

register = template.Library()
import datetime,re

@register.filter(name='cut')
def cut(value,arg):
    "Removes all values of arg from the given strings"
    return value.replace(arg,'')


@register.filter(name='lower')
def lower(value):
    "Converts a string into all lowercase"
    return value.lower()

@register.filter(name='filter_test')
def filter_test(value):
    "convert a string into all uppercase"
    return value.upper()


'''
class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)


@register.tag(name="current_time")
def current_time(parser,token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name,format_string = token.split_contents()     # 获取包含原始字符串的内容
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]   # 记录标签的名字
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])


class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return now.strftime(self.format_string)
'''

class CurrentTimeNode2(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        context['current_time2'] = now.strftime(self.format_string)
        return ''


@register.tag(name="current_time2")
def current_time2(parser,token):
    try:
        # split_contents() know not to split quoted strings.
        tag_name,format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode2(format_string[1:-1])


class CurrentTimeNode3(template.Node):
    def __init__(self,format_string,var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        # context[self.var_name] = 'this is test'
        return ''


@register.tag(name='do_current_time')
def do_current_time(parser,token):
    # this version uses a regular expression to parse tag contents.
    try:
        # splitting by None == splitting by spaces.
        # tag_name, arg = token.contents.split_contents()[0]
        tag_name, arg = token.contents.split(None,1)
    except ValueError:
        msg = "%r tag requires a single argument" % token.contents[0]
        raise template.TemplateSyntaxError(msg)

    m = re.search(r'(.*?) as (\w+)',arg)        # 正则表达式
    if m:
        fmt, var_name = m.groups()
    else:
        msg = "%r tag had invalid arguments " % tag_name
        raise template.TemplateSyntaxError(msg)

    if not (fmt[0] == fmt[-1] and fmt[0] in ('"',"'")):
        msg = "%r tag's argument should be in quotas" % tag_name
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode3(fmt[1:-1],var_name)


# 分析直之另一个模板标签
class CommentNode(template.Node):
    def render(self, context):
        return ''

@register.tag(name='do_comment')
def do_comment(parser,token):           #注释的标签
    node_list = parser.parse(('endcomment',))
    parser.delete_first_token()
    return CommentNode()


# 分析直之另一个模板标签并保存内容
class UpperNode(template.Node):
    def __init__(self,node_list):
        self.node_list = node_list

    def render(self, context):
        output = self.node_list.render(context)
        return output.upper()

@register.tag(name='doupper')
def do_upper(parser,token):
    node_list = parser.parse(('enddoupper',))
    parser.delete_first_token()
    return UpperNode(node_list)


def current_time(format_string):
    try:
        return datetime.datetime.now().strftime(str(format_string))
    except UnicodeEncodeError:
        return ''
register.simple_tag(current_time)

def new_time(format_string):
    try:
        return datetime.datetime.now().strftime(str(format_string))
    except UnicodeEncodeError:
        return ''
register.simple_tag(new_time)


@register.inclusion_tag('html/tag_books_snippet.html')
def books_for_author(author):
    books = Books.objects.filter(id=author)
    return {'books':books}

