from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),

    path('accept_blood/', views.accept_blood),
    path('blood_unit/', views.blood_unit),
    path('issue_blood/', views.issue_blood),
    path('organize_camp/', views.organize_camp),
    path('update_donor/', views.update_donor),
    path('view_camp_detail/', views.view_camp_detail),
    path('view_camp/', views.view_camp),
    path('view_donors/', views.view_donors),
    
]
