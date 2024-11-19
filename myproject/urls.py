"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),# Все URL с префиксом blog/ идут в приложение blog и дальше распределяет который находится в блоге
    path('news/', include('news.urls')),  # Все URL с префиксом news/ идут в приложение news
    path('', views.home, name='home'),  # Указываем  # Главная страница проекта
    path('search/', views.global_search, name='global_search'),  # Маршрут для поиска


]