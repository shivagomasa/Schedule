from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'schedule/task_list.html'

class TaskDetail(DetailView):
    model = Task
    template_name = 'schedule/task_detail.html'

class NewTask(CreateView):
    model = Task
    template_name = 'schedule/task_new.html'
    fields = ['title','date','time',]
