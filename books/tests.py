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

'''

