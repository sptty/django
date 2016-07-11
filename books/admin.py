from django.contrib import admin

from books.models import Publisher,Author,Books

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email',)
    search_fields = ('first_name','last_name','email',)

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date',)
    date_hierarchy = 'publication_date'
    search_fields = ('title','publisher',)
    ordering = ('publication_date',)
    # list_filter = ('publication_date',)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city','state_province','country','website')
    search_fields = ('name', 'address', 'city', 'state_province', 'country', 'website')

admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Books,BooksAdmin)

from .  import models
admin.site.register(models.Article)