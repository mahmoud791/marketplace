from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input100', 'placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'input100', 'placeholder':'Email'}),
            'password1': forms.TextInput(attrs={'class': 'input100', 'placeholder':'Password', 'type':'password', 'name':'password1'}),
            'password2': forms.TextInput(attrs={'class': 'input100', 'placeholder':'Confirm Password','type':'password','name':'password2'}),
        }
    

    # def clean(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')

    #     if password1 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")

    #     return self.cleaned_data

