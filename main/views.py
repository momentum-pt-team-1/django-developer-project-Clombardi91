from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.shortcuts import render, get_object_or_404
from .forms import TodoForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def todo_list(request):
    todos = Todo.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'main/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'main/todo_detail.html', {'todo': todo})
    

def todo_new(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.text = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'main/todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.created_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'main/todo_edit.html', {'form': form})
     
