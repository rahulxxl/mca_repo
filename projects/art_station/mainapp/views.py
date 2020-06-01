from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from . import models
from . import forms

# from .filters import OrderFilter



def homepage(request):
    i = [x for x in range(50)]
    context={'range_i': i}
    return render(request,'mainapp/homepage.html', context)


def artist_login(request):
    context={}
    return render(request, 'mainapp/artist_login.html', context)


def studio_login(request):
    context={}
    return render(request, 'mainapp/studio_login.html', context)

def studio_home(request):
    images = models.ImageStore.objects.all()
    context={'i': images}
    return render(request, 'mainapp/studio_home.html', context)

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



def artist_view_job(request):
    jobs = models.JobListing.objects.all()
    context={"jobs":jobs}
    return render(request, 'mainapp/artist_view_job.html', context)



def redirect_facebook(request):
    return redirect('https://www.facebook.com/')


def profilepage(request):
    return render(request, 'mainapp/profile.html')


def image_upload(request):
    if request.method == "POST":
        form = forms.ImageUpload(request.POST, request.FILES)
        
        if form.is_valid():
            # Cleanup the form Data
            data = form.cleaned_data
            # Create a record for image store
            img_store = models.ImageStore()
            img_store.image = data["image"]
            # Create a ImageInfoArtist
            obj = models.ImageInfoArtist()
            obj.owner = models.Artist.objects.first()
            obj.image_store = img_store
            obj.desc = data["desc"]
            obj.medium = data["medium"]
            obj.software = data["software"]
            # Save the data
            img_store.save()
            obj.save()


            return HttpResponseRedirect('/artist_home/')
    else:
        form = forms.ImageUpload()

    context = {"form":form}
    return render(request, "mainapp/image_upload.html", context)

def demo(request):
    myFilter = OrderFilter(request.GET, queryset = orders)
    
    context={"filter":myFilter}