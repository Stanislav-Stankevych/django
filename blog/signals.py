from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.postgres.search import SearchVector
from .models import Post

@receiver(post_save, sender=Post)
def update_post_search_vector(sender, instance, **kwargs):
    instance.search_vector = (
        SearchVector('title', weight='A') + SearchVector('content', weight='B')
    )
    instance.save(update_fields=['search_vector'])
