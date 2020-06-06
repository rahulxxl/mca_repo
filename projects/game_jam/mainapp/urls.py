from django.urls import path

from . import views

urlpatterns = [
    path('', views.developer_login, name="developer_login"),
    path('developer_register/', views.developer_register,name="developer_register"),
    path('developer_logout/', views.developer_logout,name="developer_logout"),
    path('developer_home/', views.developer_home, name ="developer_home"),
    path('developer_view_jam/', views.developer_view_jam, name ="developer_view_jam"),
    path('developer_apply_jam/<int:jam_id>', views.developer_apply_jam, name="developer_apply_jam"),  

    path('all_view_jam/', views.all_view_jam, name="all_view_jam"),

    path('studio_login/', views.studio_login, name="studio_login"),
    path('studio_logout/', views.studio_logout, name="studio_logout"),
    path('studio_register/', views.studio_register, name="studio_register"),
    path('studio_home/', views.studio_home, name="studio_home"),
    path('studio_create_jam/', views.studio_create_jam, name="studio_create_jam"),
    path('studio_view_jam/', views.studio_view_jam, name="studio_view_jam"),

    path('confirm_create_jam/', views.confirm_create_jam, name="confirm_create_jam"),

]
