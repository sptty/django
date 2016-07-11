# Register your models here.

from django.contrib import admin

from .models import Question,Choice


# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['question_text']}),
    ]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)

