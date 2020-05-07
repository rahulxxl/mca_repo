from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='main page'),
    path('issue/', views.bookIssue, name='book issue'),
]
