import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views import generic
#from youtubesearchpython import VideosSearch
#import wikipedia
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'dashboard/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account for {} created successfully'.format(username))
            return redirect('login')
    else:
        form = UserRegistrationForm()
    data = {'form':form}
    return render(request, 'dashboard/register.html', data)

@login_required
def profile(request):
    homeworks = Homework.objects.filter(is_finished=False, user=request.user)
    todos = ToDo.objects.filter(is_finished=False, user=request.user)
    if len(homeworks) == 0:
        homework_done = True
    else:
        homework_done = False
    if len(todos) == 0:
        todos_done = True
    else:
        todos_done = False
        
    data = {
        'homeworks':homeworks,
        'todos':todos,
        'homework_done':homework_done,
        'todos_done':todos_done
    }
    return render(request, 'dashboard/profile.html', data)

@login_required
def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            try:
                notes = Notes(
                    user=request.user,
                    title=request.POST['title'],
                    description=request.POST['description']
                )
                notes.save()
                messages.success(request, 'The notes "{}" was added successfully'.format(notes.title))
            except:
                messages.error(request, 'Failed to add note')
        else:
            messages.info(request, 'Invalid Form')
    else:
        form = NotesForm()
        return render(request, 'dashboard/notes.html', {'form':form})
    notes = Notes.objects.filter(user=request.user)
    data = {'notes':notes, 'form':form}
    return render(request, 'dashboard/notes.html', data)

@login_required
def edit_note(request, pk=None):
    form = EditNoteForm()
    note = Notes.objects.get(id=pk)
    form.fields['title'].initial = note.title
    form.fields['description'].initial = note.description
    
    
    data = {
        'form':form,
        'note':note
    }

    return render(request, 'dashboard/edit-note.html', data)

@login_required
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect('notes')

class NotesDetailView(generic.DetailView):
    model = Notes
@login_required
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

@login_required
def update_homework(request, pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

@login_required
def delete_homework(request, pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect('homework')

@login_required
def youtube(request):
    form = SearchForm()
    data = {'form':form}
    return render(request, 'dashboard/youtube.html', data)
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

@login_required
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

@login_required
def edit_todo(request, pk=None):
    form = EditToDoForm()
    todo = ToDo.objects.get(id=pk)
    form.fields['title'].initial = todo.title
    form.fields['due'].initial = todo.due
    form.fields['is_finished'].initial = todo.is_finished

    if request.method == "POST":
        form = EditToDoForm(request.POST)
        if form.is_valid():
            pk = request.POST['todo_id']
            title = form.cleaned_data['title'],
            due = form.cleaned_data['due'],
            is_finished = form.cleaned_data['is_finished']

            try:
                new_todo = ToDo.objects.get(id=pk)
                new_todo.title = title,
                new_todo.due = due,
                new_todo.is_finished = is_finished
                new_todo.save()           
                messages.success(request, '{} Edited Successfully'.format(title))
                return redirect('todo')
            except:
                messages.error(request, 'Failed to edit {}'.format(title))
                return redirect('todo')
        else:
            form = EditToDoForm()
            return render(request, 'dashboard/edit-todo.html', data)
    '''
    else:
        messages.info(request, 'Invalid response method')
        return redirect('todo')
    '''
    data = {
        'form':form,
        'todo':todo
    }

    return render(request, 'dashboard/edit-todo.html', data)

@login_required
def delete_todo(request, pk=None):
    ToDo.objects.get(id=pk).delete()
    return redirect('todo')

@login_required
def books(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        url = "https://www.googleapis.com/books/v1/volumes?q="+text
        r = requests.get(url)
        answer = r.json()
        result_list = []
        for i in range(10):
            result_dict = {
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('pageCount'),
                'categories':answer['items'][i]['volumeInfo'].get('categories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
            }
            result_list.append(result_dict)
            data = {'form':form, 'results':result_list}
        return render(request, 'dashboard/books.html', data)
    else:
        form = SearchForm()
    data = {'form':form}
    return render(request, 'dashboard/books.html', data)

@login_required
def dictionary(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"+text
        r = requests.get(url)
        answer = r.json()
        try:
            phonetics = answer[0]['phonetics'][0]['text']
            audio = answer[0]['phonetics'][0]['audio']
            definition = answer[0]['meanings'][0]['definitions'][0]['definition']
            example = answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms = answer[0]['meanings'][0]['definitions'][0]['synonyms']

            data = {
                'form':form,
                'input':text,
                'phonetics':phonetics,
                'audio':audio, 
                'definition':definition, 
                'example':example,
                'synonyms':synonyms, 
            }  
        except:
            data = {'form':form, 'input':''} 
        return render(request, 'dashboard/dictionary.html', data)
    else: 
        form = SearchForm()
        data = {'form':form,}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        return render(request, 'dashboard/dictionary.html', data)

@login_required
def wikipedia(request):
    '''
    if request.method == "POST":
        text = request.POST['text']
        form = SearchForm(request.POST)
        search = wikipedia.page(text)
        data = {
            'form':form,
            'title':search.title,
            'details':search.summary
        }
    else:
        form = SearchForm()
        data = {'form':form,}
    '''
    form = SearchForm()
    data = {'form':form,}
    return render(request, 'dashboard/wiki.html', data)

@login_required
def conversion(request):
    if request.method == "POST":
        form = ConversionForm(request.POST)    
        if request.POST['measurement'] == 'length':
            measurement_form = ConversionLengthForm()
            data = {'form':form, 'm_form':measurement_form, 'input':True}
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'yard' and second == 'foot':
                        answer = f'{input} yard={int(input)*3} foot'
                    elif first == 'foot' and second == 'yard':
                        answer = f'{input} yard={int(input)/3} yard'
                data = {'form':form, 'm_form':measurement_form, 'answer':answer, 'input':True}
        elif request.POST['measurement'] == 'mass':
            measurement_form = ConversionMassForm()
            data = {'form':form, 'm_form':measurement_form, 'input':True}
            if 'input' in request.POST:
                first = request.POST['measure1']
                second = request.POST['measure2']
                input = request.POST['input']
                answer = ''
                if input and int(input) >= 0:
                    if first == 'pound' and second == 'kilogram':
                        answer = f'{input} pound={int(input)*0.453592} kilogram'
                    elif first == 'kilogram' and second == 'pound':
                        answer = f'{input} kilogram={int(input)*2.20462} pound'
                data = {'form':form, 'm_form':measurement_form, 'answer':answer, 'input':True}
        return render(request, 'dashboard/conversion.html', data)    
    else:                
        form = ConversionForm()
        data = {'form':form, 'input':False}
    return render(request, 'dashboard/conversion.html', data)