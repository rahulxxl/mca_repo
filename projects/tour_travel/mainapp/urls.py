from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),

    path('hotel_detail/<int:hotel_id>', views.hotel_detail, name='hotel_detail'),
    path('view_hotel/', views.view_hotel, name='view_hotel'),
    path('plan_travel/', views.plan_travel, name='plan_travel'),
    path('confirmation/', views.confirmation, name='confirmation'),


]
