from django.urls import path

from . import views

urlpatterns = [
    path('',views.homepage, name="home page"),
    path('facebook/', views.redirect_facebook, name='redirect_facebook'),
    path('profile/', views.profilepage, name="Profile_Page"),
]
