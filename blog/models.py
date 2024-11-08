# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()              # Содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания поста
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления поста
    is_published = models.BooleanField(default=True)      # Поле для публикации поста

    def __str__(self):
        return self.title
