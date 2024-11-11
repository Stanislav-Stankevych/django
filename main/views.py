from django.shortcuts import render

# Create your views here.
# main/views.py
from django.shortcuts import render
from blog.models import Post
from news.models import News

def home(request):
    # Получаем последние 5 блогов и новостей
    recent_posts = Post.objects.filter(is_published=True).order_by('-created_at')[:5]
    recent_news = News.objects.filter(is_published=True).order_by('-created_at')[:5]
    context = {
        'recent_posts': recent_posts,
        'recent_news': recent_news,
    }
    return render(request, 'base.html', context)
