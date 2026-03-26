"""URL configuration for portafolio project."""

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("developer1/", include("developer1.urls")),
    path("carlos_andres/", include("carlos_andres.urls")),
]
