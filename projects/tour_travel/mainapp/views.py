from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'mainapp/homepage.html')

def login(request):
    return render(request, 'mainapp/login.html')