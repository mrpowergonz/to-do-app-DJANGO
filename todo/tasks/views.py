from django.shortcuts import render, redirect
from django.http import HttpResponse #import this
from .models import *
from .forms import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'tasks':tasks, 'form':form}#diccionario para pasarlo al template
    return render(request, 'tasks/list.html', context)#relacionarlo con el template que he creado

def updateTask(request,pk):
    task= Task.objects.get(id=pk)

    form=TaskForm(instance=task)

    if request.method == 'POST':
        form=TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request,pk):#PK es primary key
    item = Task.objects.get(id=pk)  
    #que pasa despues de darle a enviar
    if request.method == 'POST':
        item.delete()
        return redirect('/') #para que te lleve a su pagina principal
    
    #Para enlazarlo con item en delete.html
   
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)#Le paso el template 