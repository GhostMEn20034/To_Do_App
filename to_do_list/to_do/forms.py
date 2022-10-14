from django import forms
from django.forms import Textarea, TextInput, CheckboxInput

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_text', 'reminder_date', 'execution_status']
        widgets = {
            'task_title': TextInput(attrs={'class': "form-control"}),
            'task_text': Textarea(attrs={'class': "form-control", 'style': 'resize: none'}),
            'reminder_date': TextInput(
                attrs={'class': "form-control", 'id': 'date-picker'},
            ),
            'execution_status': CheckboxInput(attrs={'class': 'form-check', 'id': 'input-check-box'})

        }
