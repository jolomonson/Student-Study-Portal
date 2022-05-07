from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views import generic
#from youtubesearchpython import VideosSearch

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request, 'The notes "{}" was added successfully'.format(notes.title))
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    data = {'notes':notes, 'form':form}
    return render(request, 'dashboard/notes.html', data)

def delete_notes(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes

def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homework = Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            homework.save()
            messages.success(request, 'The homework "{}" was added successfully'.format(homework.title))
            return redirect('homework')
    else:
        form = HomeworkForm()
    homework = Homework.objects.filter(user=request.user)
    if len(homework) == 0:
        homework_done = True
    else:
        homework_done = False
    data = {'homeworks':homework, 'homework_done':homework_done, 'form':form}
    return render(request, 'dashboard/homework.html', data)

def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')

def youtube(request):
    pass
    '''
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        #video = VideosSearch(text, limit=10)
        result_list =[]
        for i in video.result()['result']:
            result_dict = {
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbnails':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewcount']['short'],
                'published':i['publishedTime'],
            }
            desc = ""
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc += j['text']
            result_dict['description'] = desc
            result_list.append(result_dict)
            data = {'form':form, 'results':result_list}
        return render(request, 'dashboard/youtube.html', data)
    else:
        form = SearchForm()
    data = {'form':form}
    return render(request, 'dashboard/youtube.html', data)'''

def todo(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            todo = ToDo(
                user=request.user,
                title=request.POST['title'],
                due=request.POST['due'],
                is_finished=finished
            )
            todo.save()
            messages.success(request, 'The ToDo "{}" was added successfully'.format(todo.title))
            return redirect('todo')
    else:
        form = ToDoForm()
    todo = ToDo.objects.filter(user=request.user)
    if len(todo) == 0:
        todo_done = True
    else:
        todo_done = False
    data = {'todos':todo, 'todo_done':todo_done, 'form':form}
    return render(request, 'dashboard/todo.html', data)