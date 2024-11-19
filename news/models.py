# news/models.py
from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector

class News (models.Model):
    title = models.CharField(max_length=200)  # Заголовок новости
    content = models.TextField(max_length=50)              # Содержание автора
    cr_avtor = models.CharField(max_length=200, default='Incognito')  # Имя автора новости
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания новости
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления
    is_published = models.BooleanField(default=True)      # Статус публикации новости
    search_vector = SearchVectorField(null=True, editable=False)
    
    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
    def get_model_name(self):
        return self.__class__.__name__.lower()
    

@receiver(post_save, sender=News)
def update_search_vector_news(sender, instance, **kwargs):
    instance.search_vector = (
        SearchVector('title', weight='A') + SearchVector('content', weight='B')
    )
    instance.save(update_fields=['search_vector'])