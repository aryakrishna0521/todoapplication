from django import forms
from django.contrib.auth.forms import UserCreationForm

from task.models import Todo,User


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2","phone"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),

        }

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["title"]