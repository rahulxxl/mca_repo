from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm


# Create your views here.

def homepage(request):
    return render(request, 'mainapp/homepage.html')


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        