from django.shortcuts import render


# Create your views here.

def todo_home(request):
    args = {}
    # if not returned it will give value error in browser.
    return render(request, template_name='todo/todo_home.html', context=args)
