import requests
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.views import generic
#from youtubesearchpython import VideosSearch
#import wikipedia

# Create your views here.
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

def edit_todo(request):
    pass

def delete_todo(request, pk=None):
    ToDo.objects.get(id=pk).delete()
    return redirect('todo')

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