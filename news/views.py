

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.core.paginator import Paginator
from .forms import SearchForm

from django.shortcuts import render
from .models import News

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def post_list(request):
    posts = News.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(posts, 2)  # Показываем по 2 записи на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog/post_list.html', context)


def create_news(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # перенаправляем на список статей
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
#генерация HTML шаблона
def post_detail(request, post_id):
    post = get_object_or_404(News, id=post_id, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})