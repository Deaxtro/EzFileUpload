from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import *
from django.contrib.auth.models import User

class EzForm(ModelForm):
    class Meta:
        model=Ez
        fields=['title','ezFile']


class SignUpForm(UserCreationForm):
    email=EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']