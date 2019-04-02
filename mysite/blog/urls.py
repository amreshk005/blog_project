from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'blog'

urlpatterns = [
   
    path('', views.post_list,name='post_list'),
    path('<id>/<slug>/',views.post_detail,name='post_detail'),
    path('post_create/',views.post_create, name="post_create"),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout')
]
