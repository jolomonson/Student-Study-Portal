from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes', views.notes, name='notes'),
    path('delete-notes/<int:pk>', views.delete_notes, name='delete-notes'),
    path('notes-detail/<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
    path('homework', views.homework, name='homework'),

]
