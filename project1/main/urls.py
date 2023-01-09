from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('reg', views.reg),
    path('Exit', views.Exit),
    path("Sort", views.Sort),
    path("Search", views.Search),
    path("Remove", views.Remove),
    path("about", views.About),
    path('Comment', views.Comment),
    path("Create", views.Create),
    path("Change", views.Change),
]