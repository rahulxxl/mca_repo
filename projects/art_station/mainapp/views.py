from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    i = [x for x in range(50)]
    context={'range_i': i}
    return render(request,'mainapp/homepage.html', context)

def redirect_facebook(request):
    return redirect('https://www.facebook.com/')