# views.py
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from blog.models import Post
from news.models import News
from .forms import SearchForm
from django.core.paginator import Paginator
from itertools import chain






def global_search(request):
    form = SearchForm(request.GET or None)
    posts = []
    articles = []

    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        if query:
            # Поиск по статьям блога
            post_vector = SearchVector('title', 'content')
            post_query = SearchQuery(query)
            posts = Post.objects.annotate(rank=SearchRank(post_vector, post_query)).filter(rank__gte=0.3).order_by('-rank')

            # Поиск по новостям
            article_vector = SearchVector('title', 'content')
            article_query = SearchQuery(query)
            articles = News.objects.annotate(rank=SearchRank(article_vector, article_query)).filter(rank__gte=0.3).order_by('-rank')

    return render(request, 'global_search_results.html', {
        'form': form,
        'posts': posts,
        'articles': articles,
    })
    


def home(request):
    # Получаем опубликованные посты и новости
    all_posts = Post.objects.filter(is_published=True)
    all_news = News.objects.filter(is_published=True)

    # Объединяем и сортируем все статьи по дате создания
    all_articles = sorted(
        chain(all_posts, all_news),
        key=lambda x: x.created_at,
        reverse=True
    )

    # Настраиваем пагинацию: 5 записей на страницу
    paginator = Paginator(all_articles, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, '../templates/home.html', context)
   
