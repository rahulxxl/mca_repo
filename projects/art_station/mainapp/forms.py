from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from . import models



class ImageUpload(forms.Form):
    desc = forms.CharField(max_length=100)
    medium = forms.ChoiceField(choices=models.ART_MEDIUM)
    software = forms.ChoiceField(choices=models.ART_SOFTWARE)
    image = forms.ImageField()
    
    desc.widget.attrs.update({"class":"form-control"})
    medium.widget.attrs.update({"class":"form-control"})
    software.widget.attrs.update({"class":"form-control"})


class PostJob(forms.Form):
    title = forms.CharField(max_length=100)
    description= forms.CharField(max_length=255, required=False)
    experience= forms.IntegerField(min_value=0, max_value=20, required=False)
    salary = forms.IntegerField(min_value=0, required=False)

    title.widget.attrs.update({"class":"form-control"})
    description.widget.attrs.update({"class":"form-control"})
    experience.widget.attrs.update({"class":"form-control"})
    salary.widget.attrs.update({"class":"form-control"})


class LoginFormArtist(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    username.widget.attrs.update({"class":"form-control", "placeholder":"username"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})


class LoginFormStudio(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    username.widget.attrs.update({"class":"form-control", "placeholder":"studio username"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})



class RegisterArtist(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    name.widget.attrs.update({"class":"form-control", "placeholder":"full name"})
    username.widget.attrs.update({"class":"form-control", "placeholder":"username"})
    email.widget.attrs.update({"class":"form-control", "placeholder":"email"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})
    password_confirm.widget.attrs.update({"class":"form-control", "placeholder":"confirm password"})


class RegisterStudio(forms.Form):
    name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)
    
    name.widget.attrs.update({"class":"form-control", "placeholder":"full name of studio"})
    username.widget.attrs.update({"class":"form-control", "placeholder":"studio username"})
    email.widget.attrs.update({"class":"form-control", "placeholder":"email"})
    password.widget.attrs.update({"class":"form-control", "placeholder":"password"})
    password_confirm.widget.attrs.update({"class":"form-control", "placeholder":"confirm password"})

