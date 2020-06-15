from django.urls import path


from . import views

urlpatterns = [
    path('',views.homepage, name="homepage"),
    path('current_weather/', views.current_weather, name="current_weather"),
    path('hourly_weather/', views.hourly_weather, name="hourly_weather"),
    path('five_day_weather/', views.five_day_weather, name="five_day_weather"),
    path('nearby_bus_stand/', views.nearby_bus_stand, name="nearby_bus_stand"),
    path('nearby_hotels/', views.nearby_hotels, name="nearby_hotels"),
]

