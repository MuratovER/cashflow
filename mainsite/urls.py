from django.urls import path
from django.shortcuts import render
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.home_page, name='home_page'),    
]