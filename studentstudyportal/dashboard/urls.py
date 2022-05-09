from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    # Notes
    path('notes', views.notes, name='notes'),
    path('delete-notes/<int:pk>', views.delete_notes, name='delete-notes'),
    path('notes-detail/<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
    # Home work
    path('homework', views.homework, name='homework'),
    path('update-homework/<int:pk>', views.update_homework, name='update-homework'),
    path('delete-homework/<int:pk>', views.delete_homework, name='delete-homework'),
    # Youtube
    path('youtube', views.youtube, name='youtube'),
    # ToDo
    path('todo', views.todo, name='todo'),
    path('edit-todo/<int:pk>', views.edit_todo, name='edit_todo'),
    path('delete-todo/<int:pk>', views.delete_todo, name='delete-todo'),
    # Books
    path('books', views.books, name='books'),
    # Dictionary
    path('dictionary', views.dictionary, name='dictionary'),
    # Wikipedia
    path('wikipedia', views.wikipedia, name='wikipedia'),
    # Conversion
    path('conversion', views.conversion, name='conversion'),
]
