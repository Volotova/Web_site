from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    task = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title':'Главная страница', 'tasks':task})

def about(request):
    return render(request, 'about.html')

def family(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма была не верной'
    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'family.html', context)