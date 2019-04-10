from django.urls import path
from Todo.views import todo_home, add_todo, complete_todo


urlpatterns = [
    path('', todo_home, name='todo_home'),
    path('add/', add_todo, name='add_todo'),
    path("complete/<int:todo_id>", complete_todo, name='complete'),
]
