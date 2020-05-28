from django.urls import path

from . import views

urlpatterns = [
    path('', views.artist_login, name="artist_login"),
    path('studio/', views.studio_login, name="stdio_login"),
    path('artist_profile/', views.artist_profile, name ="artist_profile"),

    path('create_jam/', views.CreateJam, name="create_jam"),
    path('view_jams/', views.ViewJam, name="view_jams"),
    path('apply_jam/<int:jam_id>', views.ApplyJam, name="apply_jam"),    
]
