from django.shortcuts import render

from .models import Todo

# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    return render(request, 'main/home.html', {'todos': todos})