"""
URL configuration for portafolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Portafolio Profesional</h1>
        <ul>
            <li><a href='/carlos_andres/'>Carlos Andres</a></li>
            <li><a href='/developer1/'>Developer 1</a></li>
        </ul>
    """)

urlpatterns = [
    path('', home),  # 👈 ESTO ARREGLA EL 404
    path('admin/', admin.site.urls),
    path('developer1/', include('developer1.urls')),
    path('carlos_andres/', include('carlos_andres.urls')),
]
