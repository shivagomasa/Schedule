from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Task

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'schedule/task_list.html'

class TaskDetail(DetailView):
    model = Task
    template_name = 'schedule/task_detail.html'