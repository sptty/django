from django import template
register = template.Library()

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

