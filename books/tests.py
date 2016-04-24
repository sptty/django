# -*- coding : utf-8 -*-
import os
# Create your tests here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from books.models import Publisher
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
'''

name = raw_input('What is your name')
age = raw_input('how old are you ')
sex = raw_input('are you a male or female')
job = raw_input('what is your job')
salary = raw_input('What is your salary')

print('''My name is %s,
I am %d old,
I am a %s,
I am a %s,
My salary is %s
''' % (name,age,sex,job,salary))


