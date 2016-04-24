# -*- coding : utf-8 -*-
# Create your tests here.
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# from books.models import Publisher
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

name = input('What is your name: ')
age = input('how old are you: ')
sex = input('are you a male or female: ')
job = input('what is your job: ')
salary = input('What is your salary: ')

print('''
-------------Begin---------------
The person info are blew:
My name is %s,
I am %s old,
I am a %s,
I am a %s,
My salary is %s
--------------End----------------
''' % (name,age,sex,job,salary))

