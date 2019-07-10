from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from .forms import DateTimeForm

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
    form_class = DateTimeForm

class TaskEdit(UpdateView):
    model = Task
    template_name = 'schedule/task_edit.html'
    fields = ['title','date','time']

class TaskDelete(DeleteView):
    model = Task
    template_name = 'schedule/task_delete.html'
    success_url = reverse_lazy('task_list')