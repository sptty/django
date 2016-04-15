# -*- coding : utf-8 -*-
import os
# Create your tests here.

from books.models import Publisher
'''
try:
    p = Publisher.objects.get(name='sptty')
except Publisher.DoesNotExist:
    print('sptty is not in the database yet.')
else:
    print(p)
'''
from books.models import Publisher
p1 = Publisher(name='Apress', address='2855 Telegraph Avenue',
    city='Berkeley', state_province='CA', country='U.S.A.',
    website='http://www.apress.com/')
p1.save()
p2 = Publisher(name="O'Reilly", address='10 Fawcett St.',
    city='Cambridge', state_province='MA', country='U.S.A.',
    website='http://www.oreilly.com/')
