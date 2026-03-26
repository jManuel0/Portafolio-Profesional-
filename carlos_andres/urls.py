# carlos_andres/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hoja_vida, name='carlos'),
]