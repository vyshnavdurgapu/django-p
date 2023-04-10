from django.urls import path
from . import views 

app_name='sitegroc'
urlpatterns = [
    path('',views.home,name='home'),
    path('join',views.join,name='join1')
]