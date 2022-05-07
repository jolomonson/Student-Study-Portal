from django.contrib import admin
from . models import *
# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'description'
    )
    list_filter = (
        'title',
        'description'
    )
class HomeworkAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'subject',
        'title',
        'description',
        'due',
        'is_finished',
    )
    list_filter = (
        'subject',
        'title',
        'description',
    )

admin.site.register(Notes, NotesAdmin)
admin.site.register(Homework, HomeworkAdmin)