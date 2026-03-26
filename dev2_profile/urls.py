from django.urls import path

from .views import index

app_name = 'dev2_profile'

urlpatterns = [
    path('', index, name='index'),
]
