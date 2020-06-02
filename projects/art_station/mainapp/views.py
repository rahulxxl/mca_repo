from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib import messages

from . import models
from . import forms

# from .filters import OrderFilter


def artist_logout(request):
    #logout(request)
    return redirect('artist_login')


def studio_register(request):
    pass

def studio_login(request):
    context={}
    return render(request, 'mainapp/studio_login.html', context)

def studio_logout(request):
    pass



def studio_job(request):
    if request.method == "POST":
        form = forms.PostJob(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            studio = models.Studio.objects.last()
            job = models.JobListing()
            job.title = data['title']
            job.desc= data['description']
            job.experience = data['experience']
            job.salary = data['salary']
            job.studio = studio
            job.save()

            return HttpResponseRedirect('/studio_home/')
    else:
        form = forms.PostJob()

    context={"form":form}
    return render(request, 'mainapp/studio_job.html', context)



def artist_home(request):
    images = models.ImageStore.objects.all()
    total_n = images.count()
    my_dict = {}
    n = 1
    for i in images:
        my_dict[n] = i
        n = n+1

    context={'image_data': my_dict, "total_n":total_n}
    return render(request, 'mainapp/artist_home.html', context)


def studio_home(request):
    images = models.ImageStore.objects.all()
    total_n = images.count()
    my_dict = {}
    n = 1
    for i in images:
        my_dict[n] = i
        n = n+1

    context={'image_data': my_dict, "total_n":total_n}
    return render(request, 'mainapp/studio_home.html', context)

    

def artist_images(request):
    sessions = models.ActiveSession.objects.all()
    session = sessions.last()
    images = models.ImageStore.objects.filter(owner=session.artist)

    total_n = images.count()
    my_dict = {}
    n = 1
    for i in images:
        my_dict[n] = i
        n = n+1

    context={'image_data': my_dict, "total_n":total_n}
    return render(request, 'mainapp/artist_images.html', context)


def artist_view_job(request):
    jobs = models.JobListing.objects.all()
    context={"jobs":jobs}
    return render(request, 'mainapp/artist_view_job.html', context)



def confirm_apply_job(request, job_id):
    job = models.JobApplication()
    job.job_listing = models.JobListing.objects.get(id=job_id)
    sessions = models.ActiveSession.objects.all()
    session = sessions.last()
    job.artist = session.artist
    job.save()

    context = {}
    return render(request, 'mainapp/confirm_apply_job.html', context)



def image_upload(request):
    if request.method == "POST":
        form = forms.ImageUpload(request.POST, request.FILES)
        
        if form.is_valid():
            # Cleanup the form Data
            data = form.cleaned_data
            # Create a record for image store
            sessions = models.ActiveSession.objects.all()
            session = sessions.last()
            obj = models.ImageStore()
            obj.image = data["image"]
            obj.owner = session.artist
            obj.desc = data["desc"]
            obj.medium = data["medium"]
            obj.software = data["software"]
            # Save the data
            obj.save()

            return redirect('artist_home')
    else:
        form = forms.ImageUpload()

    context = {"form":form}
    return render(request, "mainapp/image_upload.html", context)




def artist_register(request):
    if request.method == "POST":
        form = forms.RegisterArtist(request.POST)
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
                

            users = models.Artist.objects.all()
            for x in users:
                if username == x.username:
                    flagError = True
                    messages.error(request,"username already taken.")
                if email == x.email:
                    flagError = True
                    messages.error(request,"email already exists.")

            if(flagError == False):
                newArtist = models.Artist()
                newArtist.name = name
                newArtist.username =username
                newArtist.email = email
                newArtist.password = password
                newArtist.save()
                messages.success(request,"User created successfully. Please Log In")
                return redirect("artist_login")
            else:
                pass
    else:
        form=forms.RegisterArtist()
    
    context ={"form":form}
    return render(request, 'mainapp/artist_register.html',context)



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
                    messages.error(request,"studio username already taken.")
                if email == x.email:
                    flagError = True
                    messages.error(request,"studio email already exists.")

            if(flagError == False):
                newStudio = models.Studio()
                newStudio.name = name
                newStudio.username =username
                newStudio.email = email
                newStudio.password = password
                newStudio.save()
                messages.success(request,"Studio user created successfully. Please Log In")
                return redirect("studio_login")
            else:
                pass
    else:
        form=forms.RegisterStudio()
    
    context ={"form":form}
    return render(request, 'mainapp/studio_register.html',context)




def artist_login(request):
    if request.method == "POST":
        form = forms.LoginFormArtist(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uname = data["username"]
            passwd = data["password"]
            uname_comp = models.Artist.objects.all()
            for x in uname_comp:
                if x.username == uname:
                    if x.password == passwd:
                        session= models.ActiveSession()
                        session.session_type= models.ActiveSession.SESSION_TYPE[0]
                        session.artist = x  # x is model object of ArtistLogin. Thats what we want
                        session.save()
                        return redirect('artist_home')
                    else:
                        messages.error(request, "username and password does not match")
                        return redirect("artist_login")
            
            print("username does not exsits")
            messages.error(request, "username does not exists")

    else:
        form = forms.LoginFormArtist()
    
    context={"form":form}
    return render(request, 'mainapp/artist_login.html', context)


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
                        session= models.ActiveStudioSession()
                        session.artist = x 
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
