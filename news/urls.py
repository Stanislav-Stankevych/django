from django.urls import path
from . import views


# news/urls.py
urlpatterns = [
    path('', views.news_list, name='news_list'),# Главная страница со списком новостей http://127.0.0.1:8000/news/
    path('create/', views.create_news, name='create_news'),# Страница создания новой новости http://127.0.0.1:8000/news/create/
    path('<int:news_id>/', views.news_detail, name='news_detail'),  # Детальная страница новости http://127.0.0.1:8000/news/2/
]
