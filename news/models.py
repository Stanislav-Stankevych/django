# news/models.py
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)  # Заголовок новости
    content = models.TextField()              # Содержание новости
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания новости
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления
    is_published = models.BooleanField(default=True)      # Статус публикации новости

    def __str__(self):
        return self.title
