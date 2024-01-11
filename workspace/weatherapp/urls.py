from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name = "home"),
]

handler404 = 'weatherapp.views.error_404_view'
handler404 = 'weatherapp.views.error_500'
