from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:cust_id>', views.customer, name="customer"),

    path('create_order/', views.createOrder, name="create_order"),
]
