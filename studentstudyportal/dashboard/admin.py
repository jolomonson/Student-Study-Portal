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

class ToDoAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'due',
        'is_finished',
    )
    list_filter = (
        'title',
    )

admin.site.register(Notes, NotesAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(ToDo, ToDoAdmin)