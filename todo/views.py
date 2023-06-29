from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.
def index(reqest):
    if reqest.method == 'POST':
        task = Task(title=reqest.POST['title'], due_at=make_aware(parse_datetime(reqest.POST['due_at'])))
        task.save()
    
    tasks = Task.objects.all()

    context = {
        'tasks': tasks
    }
    return render(reqest, 'todo/index.html', context)
