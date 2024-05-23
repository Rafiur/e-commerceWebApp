from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User #comes from django's auth forms
        # now we include the fields we want to view
        fields = ('username', 'email', 'password1', 'password2')
        
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-enter your passwrod',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

