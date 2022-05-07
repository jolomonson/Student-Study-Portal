from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete-notes/<int:pk>', views.delete_notes, name='delete-notes'),
    path('notes-detail/<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
    path('homework', views.homework, name='homework'),
    path('update-homework/<int:pk>', views.update_homework, name='update-homework'),
    path('delete-homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('youtube', views.youtube, name='youtube'),
    path('todo', views.todo, name='todo'),
    path('edit-todo/<int:pk>', views.edit_todo, name='edit_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete-todo'),
]
