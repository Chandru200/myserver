from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login_user',views.login_user),
    path('register',views.register),
    path('logout',views.logout_user),
    path('getuser',views.getuser),
    path("",views.home)
]
