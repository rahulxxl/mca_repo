from django.shortcuts import render


#from . import assist_data
# Create your views here.

def homepage(request):
    return render(request, "mainapp/homepage.html")

def current_weather(request):
    return render(request, "mainapp/current_weather.html")

def hourly_weather(request):
    return render(request, "mainapp/hourly_weather.html")

def five_day_weather(request):
    return render(request, "mainapp/five_day_weather.html")

def nearby_bus_stand(request):
    return render(request, "mainapp/nearby_bus_stand.html")

def nearby_hotels(request):
    return render(request, "mainapp/nearby_hotels.html")
