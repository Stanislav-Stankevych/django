# blog/models.py
from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector

class Post(models.Model):
    title = models.CharField(max_length=200)  # Заголовок поста
    content = models.TextField()              # Содержание поста
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания поста
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления поста
    is_published = models.BooleanField(default=True)      # Поле для публикации поста
    search_vector = SearchVectorField(null=True, editable=False)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
    def get_model_name(self):
        return self.__class__.__name__.lower()
    

