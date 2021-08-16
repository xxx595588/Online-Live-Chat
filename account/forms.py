from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Enter your email address here'}))
    username = forms.CharField(max_length=60, widget= forms.TextInput(attrs={'placeholder':'Enter your user name here'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Enter your first name here'}))
    last_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'placeholder':'Enter your last name here'}))
    password1 = forms.CharField(label='Password', max_length=100, widget= forms.PasswordInput(attrs={'placeholder':'Enter your password here'}))
    password2 = forms.CharField(label='Password(Confirm)', max_length=100, widget= forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))

    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
