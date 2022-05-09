from django import forms
from .models import *
from django.forms import widgets

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']

class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, label='What do you want to search ')

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        widgets = {'due':DateInput()}
        fields = ['title','due','is_finished']

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
