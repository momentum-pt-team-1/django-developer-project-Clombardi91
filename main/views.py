from django.shortcuts import render
from django.utils import timezone
from .models import Todo
from django.shortcuts import render, get_object_or_404
from .forms import TodoForm


# Create your views here.


def todo_list(request):
    todos = Todo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'main/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'main/todo_detail.html', {'todo': todo})

def todo_new(request):
    form = TodoForm()
    return render(request, 'main/todo_edit.html', {'form': form})   
