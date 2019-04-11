from django import forms
from .models import Todo


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Task',
        'name': 'task',
        'id': 'task',
        'aria-label': 'Todo',
        'aria-describedby': 'add-btn',
    }))


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'task',
                'id': 'task',
                'placeholder': 'Enter Your Task Here',
                'aria-label': 'Todo',
                'aria-describedby': 'add-btn',
            })
        }
