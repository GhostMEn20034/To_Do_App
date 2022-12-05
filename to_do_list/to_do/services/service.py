import json
from django.shortcuts import get_object_or_404
from ..models import Task


def update_execution_status_field(request):
    if request.method == 'POST':
        data = json.load(request)
        todo = data.get('payload')
        task = get_object_or_404(Task, id=todo['id'])
        task.execution_status = not task.execution_status
        task.save()
        status = 1
        done = task.execution_status
        return {
            'status': status,
            'done': done,
        }
