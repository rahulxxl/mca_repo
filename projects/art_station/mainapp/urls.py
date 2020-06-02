from django.urls import path

from . import views

urlpatterns = [
    path('',views.artist_login, name="artist_login"),
    path('artist_register/', views.artist_register, name="artist_register"),
    path('artist_logout',views.artist_logout, name="artist_logout"),
    
    path('artist_home/', views.artist_home, name="artist_home"),   
    path('artist_images/', views.artist_images, name="artist_images"),   
    path('artist_view_job/', views.artist_view_job, name="artist_view_job"),
    path('confirm_apply_job/<int:job_id>',views.confirm_apply_job, name="confirm_apply_job"),

    path('studio_login/',views.studio_login, name="studio_login"),
    path('studio_register/',views.studio_register, name="studio_register"),
    path('studio_job/', views.studio_job, name="studio_job"),
    path('studio_home/', views.studio_home, name="studio_home"),



    path('image_upload/', views.image_upload, name="image_uplod"),

    # path('facebook/', views.redirect_facebook, name='redirect_facebook'),
    # path('profile/', views.profilepage, name="Profile_Page"),

]
