from django.urls import path
from Todo.views import todo_home, add_todo, complete_todo, delete_completed, delete_all

app_name = 'todo'
urlpatterns = [
    path('', todo_home, name='todo_home'),
    path('add/', add_todo, name='add_todo'),
    path("complete/<int:todo_id>", complete_todo, name='complete'),
    path('delete_complete', delete_completed, name='delete_complete'),
    path('delete_all', delete_all, name='delete_all'),

]
