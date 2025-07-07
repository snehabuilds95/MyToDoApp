from django.shortcuts import render, redirect

from django.http import HttpResponse

from .models import Task

from  .forms import TaskForm

def index(requests):

    #return HttpResponse("Hello, world. You're at the tasks index.") 
    form = TaskForm() 

    tasks = Task.objects.all()

    if requests.method == 'POST':

        form = TaskForm(requests.POST)

        if form.is_valid():

            form.save()
            
        return redirect('/')


    context = {'tasks': tasks, 'TaskForm': form}

    return render(requests, 'tasks.html', context)

   
def updateTask(requests, pk):

    task = Task.objects.get(id=pk) # Grab and compare the primary key (pk) of the task

    form = TaskForm(instance=task) #Inside the TaskForm, 
                                   #we pass the instance of the task we want to update


    if requests.method == 'POST':

        form = TaskForm(requests.POST, instance=task)

        if form.is_valid():

            form.save()
            return redirect('/')
        

    context = {'TaskForm': form}

    return render(requests, 'update-task.html', context)


def deleteTask(requests, pk):

    task = Task.objects.get(id=pk)

    if requests.method == 'POST':

        task.delete()
        return redirect('/')

    context = {'task': task}

    return render(requests, 'delete-task.html', context)

