from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_home(request):
    todo_list = Todo.objects.order_by('id')
    args = {'todo_list': todo_list}
    # if a value not returned it will give value error in browser.
    return render(request, template_name='todo/todo_home.html', context=args)
