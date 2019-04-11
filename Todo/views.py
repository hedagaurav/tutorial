from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, NewTodoForm


# Create your views here.
def todo_home(request):
    todo_list = Todo.objects.order_by('id')
    # form = TodoForm()
    new_todo_form = NewTodoForm
    args = {'todo_list': todo_list, 'form': new_todo_form}
    # if a value not returned it will give value error in browser.
    return render(request, template_name='todo/todo_home.html', context=args)


@require_POST
def add_todo(request):
    # form = TodoForm(request.POST)
    form = NewTodoForm(request.POST)
    print(request.POST['text'])
    if form.is_valid:

        form.save()

    return redirect('todo_home')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    return redirect('todo_home')


def delete_completed(request):
    obj = Todo.objects.filter(complete__exact=True)

    if obj:
        print("obj = ", obj)
        print('%s is deleted.' % obj)
    else:
        print("obj = ", obj)
        print('empty')
    obj.delete()
    return redirect('todo_home')


def delete_all(request):
    obj = Todo.objects.all()
    obj.delete()
    return redirect('todo_home')
