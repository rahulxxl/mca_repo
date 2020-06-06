from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from . import forms
from . import models


def all_view_jam(request):
    all_jams = models.Jam.objects.all()
    jams = []
    for obj in all_jams:
        jams.append(obj)
    context = {"jams":jams,}
    return render(request, "mainapp/jam_view.html", context)


def developer_home(request):
    all_jams = models.Jam.objects.all()
    jams = []
    for obj in all_jams:
        jams.append(obj)
    context = {"jams":jams,}
    return render(request, 'mainapp/developer_home.html', context)


def developer_view_jam(request):
    all_jams = models.Jam.objects.all()
    jams = []
    for obj in all_jams:
        jams.append(obj)

    context = {"jams":jams,}
    return render(request, "mainapp/developer_view_jam.html", context)




def developer_apply_jam(request, jam_id):
    temp = models.Jam.objects.get(id=jam_id)
    context={
        "jam_id":jam_id,
        "theme":temp.theme,
        "studio":temp.studio.name,
        "start_date":temp.start_date.strftime("%d-%m-%Y"),
        "end_date":temp.end_date.strftime("%d-%m-%Y"),
        "prize":temp.prize,
    }
    return render(request, "mainapp/jam_apply.html", context)


def  studio_home(request):
    return render(request, 'mainapp/studio_home.html')


def studio_create_jam(request):
    if request.method == "POST":
        form = forms.CreateJam(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            obj = models.Jam(
                theme=data["jam_title"],
                team_size= data["team_size"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                prize=data["prize"]
            )
            obj.save()
            return redirect('confirm_create_jam')
    else:
        form = forms.CreateJam()
    return render(request, 'mainapp/studio_create_jam.html', {"form":form})



def studio_view_jam(request):
    return render(request, 'mainapp/studio_view_jam.html')


def confirm_create_jam(request):
    return render(request, 'mainapp/confirm_create_jam.html')






def developer_login(request):
    if request.method == "POST":
        form = forms.LoginFormDeveloper(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            passwd = data["password"]
            uname_comp = models.Developer.objects.all()
            for x in uname_comp:
                if x.username == uname:
                    if x.password == passwd:
                        session= models.SessionDeveloper()
                        session.developer = x
                        session.save()
                        return redirect('developer_view_jam')
                    else:
                        messages.error(request, "username and password does not match")
                        return redirect("developer_login")
            messages.error(request, "username does not exists")
    else:
        form = forms.LoginFormDeveloper()
    context={"form":form}
    return render(request, 'mainapp/developer_login.html', context)


def developer_register(request):
    if request.method == "POST":
        form = forms.RegisterDeveloper(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            username= data['username']
            email = data['email']
            password=data['password']
            password_confirm = data["password_confirm"]
            flagError =False
            if password != password_confirm:
                flagError = True
                messages.error(request,"Passwords do not match")
            users = models.Developer.objects.all()
            for x in users:
                if username == x.username:
                    flagError = True
                    messages.error(request,"username already taken.")
                if email == x.email:
                    flagError = True
                    messages.error(request,"email already exists.")
            if(flagError == False):
                newDeveloper = models.Developer()
                newDeveloper.name = name
                newDeveloper.username =username
                newDeveloper.email = email
                newDeveloper.password = password
                newDeveloper.save()
                messages.success(request,"User created successfully. Please Log In")
                return redirect("developer_login")
            else:
                pass
    else:
        form=forms.RegisterDeveloper()
    context ={"form":form}
    return render(request, 'mainapp/developer_register.html', context)


def studio_login(request):
    if request.method == "POST":
        form = forms.LoginFormStudio(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            passwd = data["password"]
            uname_comp = models.Studio.objects.all()
            for x in uname_comp:
                if x.username == uname:
                    if x.password == passwd:
                        session= models.SessionStudio()
                        session.studio = x
                        session.save()
                        return redirect('studio_home')
                    else:
                        messages.error(request, "username and password does not match")
                        return redirect("studio_login")
            messages.error(request, "username does not exists")
    else:
        form = forms.LoginFormStudio()
    context={"form":form}
    return render(request, 'mainapp/studio_login.html', context)


def studio_register(request):
    if request.method == "POST":
        form = forms.RegisterStudio(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data['name']
            username= data['username']
            email = data['email']
            password=data['password']
            password_confirm = data["password_confirm"]
            flagError =False
            if password != password_confirm:
                flagError = True
                messages.error(request,"Passwords do not match")
            users = models.Studio.objects.all()
            for x in users:
                if username == x.username:
                    flagError = True
                    messages.error(request,"username already taken.")
                if email == x.email:
                    flagError = True
                    messages.error(request,"email already exists.")
            if(flagError == False):
                newStudio = models.Studio()
                newStudio.name = name
                newStudio.username =username
                newStudio.email = email
                newStudio.password = password
                newStudio.save()
                messages.success(request,"User created successfully. Please Log In")
                return redirect("studio_login")
            else:
                pass
    else:
        form=forms.RegisterDeveloper()
    context ={"form":form}
    return render(request, 'mainapp/studio_register.html', context)


def developer_logout(request):
    models.SessionDeveloper.objects.all().delete()
    return redirect('developer_login')


def studio_logout(request):
    models.SessionStudio.objects.all().delete()
    return redirect('studio_login')

