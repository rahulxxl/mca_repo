from django.urls import path

from . import views

urlpatterns = [
    path('',views.artist_login, name="artist_login"),
    path('studio/',views.studio_login, name="studio_login"),
    path('studio_job/', views.studio_job, name="studio_job"),
    path('studio_home/', views.studio_home, name="studio_home"),

    path('artist_home/', views.artist_home, name="artist_home"),   
    path('artist_view_job/', views.artist_view_job, name="artist_view_job"),

    path('image_upload/', views.image_upload, name="image_uplod"),

    # path('facebook/', views.redirect_facebook, name='redirect_facebook'),
    # path('profile/', views.profilepage, name="Profile_Page"),

]
