from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import forms
from . import models

def login(request):
    return render(request, 'mainapp/login.html')

def hotel_detail(request, hotel_id):
    rooms = models.HotelRoom.objects.filter(id=hotel_id)
    context={"rooms":rooms}
    return render(request, 'mainapp/hotel_detail.html', context)


def view_hotel(request):
    hotels = models.Hotel.objects.all()
    context={"hotels":hotels}
    return render(request, 'mainapp/view_hotel.html', context)


def plan_travel(request):
    if request.method == "POST":
        form = forms.PlanForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data


            return HttpResponseRedirect("/view_hotel/")
    else:
        form = forms.PlanForm()
    
    context={"form":form}
    return render(request, 'mainapp/plan_travel.html', context)


def confirmation(request):
    return render(request, 'mainapp/confirmation.html')