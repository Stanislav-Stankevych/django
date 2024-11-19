from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='news_list'),
    #path('article/', views.article_list, name='article_list'),
    path('create/', views.create_news, name='create_news'),  # добавляем новый маршрут
    path('<int:post_id>/', views.post_detail, name='news_detail'),  # Детальная страница поста
]
