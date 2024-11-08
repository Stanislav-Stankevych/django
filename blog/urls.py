from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.article_list, name='article_list'),
    path('create/', views.create_post, name='create_post'),  # добавляем новый маршрут
    path('<int:post_id>/', views.post_detail, name='post_detail'),  # Детальная страница поста
]
