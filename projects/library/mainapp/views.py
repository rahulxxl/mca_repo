from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.
def mainpage(request):
    param1 = 10
    
    context = {
        'param1':param1,
    }
    return render(request, 'mainapp/homepage.html', context)


def bookIssue(request):
    return render(request, 'mainapp/book_issue.html')

