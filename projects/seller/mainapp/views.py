from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from . import models, forms


def loginPage(request):
    context={}
    return render(request, "mainapp/login.html")

def addProduct(request):
    if request.method == "POST":
        form = forms.Product(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prod = models.Product()
            
            # Get hold of customer somehow
            cust= 1231
            prod.customer =         cust
            prod.name =             data["name"]
            prod.short_description= data["short_description"]
            prod.full_description = data["full_description"]
            prod.category =         data["category"]
            prod.price =            data["price"]
            prod.image_1 =          data["image_1"]
            prod.image_2 =          data["image_2"]
            prod.image_3 =          data["image_3"]
            prod.image_4 =          data["image_4"]

            prod.save()
            return HttpResponseRedirect("/product_add_confirmation/")

    else:
        form = forms.Product()

    context={"form":form}
    return render(request, 'mainapp/product_add.html', context)


def updateProduct(request, prod_id):
    prod = models.Product.objects.get(id=prod_id)
    context={}
    if request.method == "POST":
        form = forms.Product(request.POST)
        if form.is_valid():
            data = form.cleaned_data

    else:
        data ={}
        data["name"] = prod.name
        data["short_description"] = prod.short_description
        data["full_description"] = prod.full_description
        data["category"] = prod.category
        data["price"] = prod.price
        data["image_1"] = prod.image_1
        data["image_2"] = prod.image_2
        data["image_3"] = prod.image_3
        data["image_4"] = prod.image_4
        form = forms.Product(data)

    context={"form":form}
    return render(request, 'mainapp/product_detail.html', context)        

def registerCustomer(request):
    context = {}
    return render(request, 'mainapp/customer_register.html', context)