from django.conf.urls import url,patterns

from books.views import year_archive

urlpatterns = patterns(
    'books.views',
    url(r'(?P<year>\d{4})/$',year_archive,name='year_archive'),
    # url(r'articles/[0-9]{4}/[0-9]{2}/$', month_archive, name='month_archive'),
    # url(r'articles/[0-9]{4}/[0-9]{2}/([0-9]+)/$', archive_detail, name=' archive_detail'),
)
