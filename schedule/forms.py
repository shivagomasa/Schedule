from django import forms
from .models import Task
from django.forms import ModelForm


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class DateTimeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','date','time']
        widgets = {'date':DateInput(),'time':TimeInput()}