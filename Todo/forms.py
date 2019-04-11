from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Task',
        'name': 'task',
        'id': 'task',
        'aria-label': 'Todo',
        'aria-describedby': 'add-btn',
    }))
