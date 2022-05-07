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

admin.site.register(Notes, NotesAdmin)