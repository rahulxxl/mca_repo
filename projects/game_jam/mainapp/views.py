from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms


from . import forms
from . import models


def artist_login(request):
    return render(request, 'mainapp/artist_login.html')


def studio_login(request):
    return render(request, 'mainapp/studio_login.html')

def artist_profile(request):
    return render(request, 'mainapp/artist_profile.html')


def CreateJam(request):
    if request.method == "POST":
        form = forms.CreateJam(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            obj = models.Jam(theme=data["jam_title"],
            team_size= data["team_size"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            prize=data["prize"]
            )
            obj.save()

            return HttpResponseRedirect('/')
    else:
        form = forms.CreateJam()

    return render(request, 'mainapp/createjam.html', {"form":form})


def ViewJam(request):
    all_jams = models.Jam.objects.all()
    jams = []
    for obj in all_jams:
        jams.append(obj)

    context = {"jams":jams,}
    return render(request, "mainapp/view_jams.html", context)


def ApplyJam(request, jam_id):
    temp = models.Jam.objects.get(id=jam_id)
    context={
        "jam_id":jam_id,
        "theme":temp.theme,
        "studio":temp.studio.name,
        "start_date":temp.start_date.strftime("%d-%m-%Y"),
        "end_date":temp.end_date.strftime("%d-%m-%Y"),
        "prize":temp.prize,
    }

    return render(request, "mainapp/apply_jam.html", context)

