from django.contrib import admin
from django.urls import path
from . import views
from . import todo_view
urlpatterns = [
    path('login_user',views.login_user),
    path('register',views.register),
    path('logout',views.logout_user),
    path('getuser',todo_view.get_all_todo),
    path("",views.home),
    path('get_todos',todo_view.get_all_todo),
    path('create_todo',todo_view.create_todo),
    path('edit_todo',todo_view.edit_todo),
    path('delete_todo',todo_view.delete_todo),
]
