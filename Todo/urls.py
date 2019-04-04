from django.urls import path
from Todo.views import todo_home

urlpatterns = [
    path('home/', todo_home, name='todo_home'),
]
