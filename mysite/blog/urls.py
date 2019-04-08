from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'

urlpatterns = [
    path('<id>/post_edit/',views.post_edit,name="post_edit"),
    path('<id>/post_delete/',views.post_delete,name="post_delete"),
    path('<id>/favourite_post/',views.favourite_post,name="favourite_post"),
    path('', views.post_list,name='post_list'),
    path('/<id>/<slug>/',views.post_detail,name='post_detail'),
    path('post_create/',views.post_create, name="post_create"),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('register/',views.register, name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('like/',views.like_post,name='like_post'),
    path('favourite/', views.post_favourite_list, name="post_favourite_list")

]
