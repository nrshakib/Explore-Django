from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task

def task_list(request):
    task = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/taskList.html', {'tasks': task})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()

        if title:
            Task.objects.create(title = title, description = description)
            return redirect(reverse('todo: taskList'))
        error = 'Title can not be empty'
        return render(request, 'todo/taskForm.html', {'error' : error})
    
    return render(request, 'todo/taskForm.html')

def edit_task(request, taskID):
    task = get_object_or_404(Task, taskID = taskID)

    if request.method == "POST":
        title = request.POST.get('title','').strip()
        description = request.POST.get('description','').strip()
        completed = request.POST.get('completed') == 'on'

        if title:
            task.title = title
            task.description = description
            task.completed = completed
            task.save()
            return redirect(reverse('todo:taskList'))
        return render(request, 'todo/taskForm.html', {'task': task, 'error': 'Title can not be empty'})
    
    return render(request, 'todo/taskForm.html', {'task': task})

def delete_task(request, taskID):
    task = get_object_or_404(Task, taskID = taskID)
    if request.method == "POST":
        task.delete()
        return redirect(reverse('todo:taskList.html'))

    return render(request, 'todo/taskDelete.html', {'task': task})

def toggle_task(request):
    return render(request, 'taskList.html')

