from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('test/', views.testView, name="test_page"),
    path('controls/', views.controls, name="controls"),
]
