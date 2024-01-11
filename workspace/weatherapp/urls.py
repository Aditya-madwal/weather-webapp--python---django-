from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name = "home"),
    path('weather/', views.weatherview, name = "weather")
]
