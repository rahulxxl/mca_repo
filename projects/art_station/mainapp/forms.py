from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from . import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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
    
    username.widget.attrs.update({"class":"form-control"})
    password.widget.attrs.update({"class":"form-control"})

    def clean_username(self):
        data = self.cleaned_data.get("username")
        unames = models.ArtistLogin.objects.all()
        for i in unames:
            if i == data:
                raise forms.ValidationError('Username Already exists')

        return data


