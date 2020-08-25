from django.shortcuts import render
from .models import task

# Create your views here.
def home(request):
    status = {'success': False}
    if request.method=='POST':
        taskTitle = request.POST['taskTitle']
        taskDesc = request.POST['taskDesc']
        newTask = task(taskTitle= taskTitle, taskDesc=taskDesc)
        newTask.save()
        status = {'success': True}
    return render(request, 'index.html', status)

def tasks(request):
    return render(request, 'tasks.html')
