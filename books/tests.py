# -*- coding : utf-8 -*-
import os
# Create your tests here.

__author__ = 'sptty'


from books.models import Publisher
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()

try:
    p = Publisher.objects.get(name='sptty')
except Publisher.DoesNotExist:
    print 'sptty is not in the database yet.'
else:
    print p
