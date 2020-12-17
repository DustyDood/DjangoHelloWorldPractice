from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('<int:pk>/details/', views.user_details, name="user_details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('confirm_delete/', views.confirmed, name="confirm"),
    ]

