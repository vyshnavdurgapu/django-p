from django.contrib import admin
from django.urls import path,include
from hcsv import views
from django.shortcuts import render

urlpatterns = [
    path('',views.home,name="home")
]
