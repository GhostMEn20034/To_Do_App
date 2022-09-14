from django import forms
from django.forms import Textarea

from  .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'reminder_date', ]
