from django import forms
from .models import UserRegistrationModel

'''
class UserProfile(forms.ModelForm):
    class Meta:
        model = UserRegistrationModel
        fields = ['username', 'password']
'''


class UserProfile1(forms.Form):
    username = forms.CharField(label='Username', max_length=32, widget=(forms.TextInput(attrs={
        'placeholder': 'Enter username',
    })))

    password = forms.CharField(label='Password', max_length=32, widget=(forms.TextInput(attrs={
        'placeholder': 'Enter password',
    })))
