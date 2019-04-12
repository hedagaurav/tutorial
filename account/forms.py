from django import forms
from .models import UserRegistrationModel


class UserProfile(forms.ModelForm):
    class Meta:
        model = UserRegistrationModel
        fields = ['username', 'password']
