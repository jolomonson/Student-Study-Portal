from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    data = {'notes':notes}
    return render(request, 'dashboard/notes.html', data)
