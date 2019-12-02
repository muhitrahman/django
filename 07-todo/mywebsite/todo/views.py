

from django.shortcuts import render, redirect
from .models import Todo
from .forms import DoForm
from django.views.decorators.http import require_POST


def index(request):
    mytodo = Todo.objects.order_by('id')
    form = DoForm()
    context = {'mytodo': mytodo, 'form': form}

    return render(request, 'todo/index.html', context)


@require_POST
def newTodo(request):
    form = DoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(todotext=request.POST['text'])
        new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True
    mytodo.save()

    return redirect('index')


def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')

