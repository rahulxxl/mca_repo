from django import forms


from . import models


class Customer(forms.Form):
    name = forms.CharField(max_length=70, required= False)
    company = forms.CharField(max_length=100, required=False)
    gstin =forms.CharField(max_length=15, required =False)
    email = forms.EmailField(max_length=50, required =False)
    phone = forms.CharField(max_length=15, required=True)

    name.widget.attrs.update({"class":"form-control"})
    company.widget.attrs.update({"class":"form-control"})
    gstin.widget.attrs.update({"class":"form-control"})
    email.widget.attrs.update({"class":"form-control"})
    phone.widget.attrs.update({"class":"form-control"})


class Product(forms.Form):
    product_name= forms.CharField(max_length=100)
    short_description = forms.CharField(max_length=140, widget=forms.Textarea)
    full_description= forms.CharField(max_length=1000, widget= forms.Textarea, required=False)
    category = forms.ChoiceField(choices=models.CATEGORY)
    price = forms.IntegerField(min_value=0)
    image_1 = forms.ImageField(required=False)
    image_2 = forms.ImageField(required=False)
    image_3 = forms.ImageField(required=False)
    image_4 = forms.ImageField(required=False)

    product_name.widget.attrs.update({"class":"form-control"})
    short_description.widget.attrs.update({"class":"form-control"})
    full_description.widget.attrs.update({"class":"form-control"})
    category.widget.attrs.update({"class":"form-control"})
    price.widget.attrs.update({"class":"form-control"})
    