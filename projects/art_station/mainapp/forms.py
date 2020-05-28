from django.contrib.auth.forms import UserCreationForm
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

