# -*- coding : utf-8 -*-
# Create your tests here.

'''
try:
    p = Publisher.objects.get(name='sptty')
except Publisher.DoesNotExist:
    print('sptty is not in the database yet.')
else:
    print(p)

from books.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
    city='Berkeley', state_province='CA', country='U.S.A.',
    website='http://www.apress.com/')
p1.save()
p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
    city='Cambridge', state_province='MA', country='U.S.A.',
    website='http://www.oreilly.com/')


from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Books


if 'q' in request.GET and request.GET['q']:
    q = request.GET['q']
    books = Books.objects.filter(title__icontains=q)
    print(books)
    return render_to_response('html/form_search_result.html', {'title': 'Search results', '': books})

else:
    HttpResponse('Please submit a search term')




name = [3,5,66,3,99,33,545,3,2,6,888,5555,6,5,399]
print(sorted(name)[-2:])


def test(name,age,weight):
    print('My name is '+name + ',I am  '+ age +' years old, I am '+  weight)

test(name='sptty',weight='70',age='26')

sums = 1
for i in range(1,362):
    sums *= i
    if i ==361:
        print(str(sums))



def foo(*args,**kwargs):
    print('Postional argument are:')
    print(args)
    print('keyword argument are:')
    print(kwargs)
    kwarg = kwargs.pop('a')
    print(kwarg)
    print(kwargs)


print({'d':1,'e':2,'f':3,},foo(a=1,b=2,c=3))


from mysite.views import custom_proc
print(custom_proc.__doc__)

'''


def g(n):
    for i in range(n):
        yield i**2

for i in g(5):
    print(i)


for i in range(5):
    print(i**2)




a = 'this is a test'

from books.models import Books

books11 = Books.objects
print(books11)


import ansible.runner
runner = ansible.runner.Runner(
    module_name = 'ping',
    module_args = '',
    pattern = 'web',
    forks = 0,
)

datastructure = runner.run()