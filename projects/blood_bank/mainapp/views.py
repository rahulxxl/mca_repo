from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import *
# from .urls import urlpatterns


def homepage(request):
    context = {}
    return render(request, 'mainapp/homepage.html', context)


def accept_blood(request):
    context = {}
    return render(request, 'mainapp/accept_blood.html', context)


def blood_unit(request):
    context = {}
    return render(request, 'mainapp/blood_unit.html', context)


def issue_blood(request):
    context = {}
    return render(request, 'mainapp/issue_blood.html', context)


def organize_camp(request):
    context = {}
    return render(request, 'mainapp/organize_camp.html', context)


def update_donor(request):
    context = {}
    return render(request, 'mainapp/update_donor.html', context)

    
def view_camp_detail(request):
    context = {}
    return render(request, 'mainapp/view_camp_detail.html', context)


def view_camp(request):
    context = {}
    return render(request, 'mainapp/view_camp.html', context)


def view_donors(request):
    return render(request, 'mainapp/view_donors.html')
































def testView(request):
    # if this is a POST request, means we have some data on our form.
    if request.method == "POST" :
        # create a form instance to hold the data passed by the browser. Construct it with recieved data
        my_form = TestForm(request.POST)
        # check if it is valid
        if my_form.is_valid():
            # TODO: You have the valid Data.
            # Process that data here
            final_data = my_form.cleaned_data
            # ......
            # ......
            
            # Redirect to new URL
            print("++++++++++++The Donor Info is  :: ", final_data)
            return HttpResponseRedirect("/")
    
    # This is a GET request. Create a Blank form here
    else:
        my_form = TestForm()

    return render(request, 'mainapp/test_page.html', {'form' : my_form})


def controls(request):
    if request.method =="POST":
        my_form = ViewControls(request.POST)

        if my_form.is_valid():
            final_data = my_form.cleaned_data

            return HttpResponseRedirect("/")

    else:
        my_form = ViewControls()

    return render(request, 'mainapp/controls.html', {"form" : my_form})
    