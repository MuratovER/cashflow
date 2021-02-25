from django.urls import path
from django.shortcuts import render
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('input/data_input', views.data_input, name='data_input'),




]