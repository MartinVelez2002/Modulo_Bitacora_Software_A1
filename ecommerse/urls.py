"""
URL configuration for ecommerse project.

The `urlpatterns` list routes URLs to views_docentes. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views_docentes
    1. Add an import:  from my_app import views_docentes
    2. Add a URL to urlpatterns:  path('', views_docentes.home, name='home')
Class-based views_docentes
    1. Add an import:  from other_app.views_docentes import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ecommerse.viewsIndex import IndexTemplate


urlpatterns = [
    path('', IndexTemplate.as_view()),
    path('docentes/', include('modulos.Docentes.urls')),
    path('actividad/', include('modulos.Actividades.urls')),
    path('login_mod/', include('modulos.Login.urls')),
]
