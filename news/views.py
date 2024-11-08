# news/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm

# Представление для списка новостей
def news_list(request):
    news_items = News.objects.filter(is_published=True).order_by('-created_at')  # Показываем только опубликованные новости
    return render(request, 'news/news_list.html', {'news_items': news_items})

# Представление для детальной страницы новости
def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)  # Находим новость по id или возвращаем 404
    return render(request, 'news/news_detail.html', {'news_item': news_item})

# Представление для создания новой новости
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Перенаправляем на список новостей после сохранения
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

# news/views.py
def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id, is_published=True)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

# views.py


def track_refresh(request):
    # Проверяем, есть ли в сессии счётчик обновлений
    if 'refresh_count' in request.session:
        request.session['refresh_count'] += 1  # Увеличиваем счётчик на 1
    else:
        request.session['refresh_count'] = 1  # Инициализируем счётчик

    # Получаем значение счётчика из сессии
    refresh_count = request.session['refresh_count']
    
    # Передаем счётчик в шаблон
    return render(request, 'news/news_detail.html', {'refresh_count': refresh_count})
