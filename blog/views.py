

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

#def article_list(request):
 #   articles = Post.objects.all()
  #  return render(request, 'blog/article_list.html', {'articlesscilk': articles})

def article_list(request):
    posts = Post.objects.order_by('-created_at')  # Сортируем по дате создания, самые новые сверху
    paginator = Paginator(posts, 2)  # Показываем по 2 статьи на странице

    page_number = request.GET.get('page')  # Получаем номер страницы из параметра GET
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'blog/article_list.html', {'page_obj': page_obj})

#def post_list(request):
 #   posts = Post.objects.all()
  #  return render(request, 'blog/post_list.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.order_by('-created_at')  # Сортируем по дате создания, самые новые сверху
    paginator = Paginator(posts, 2)  # Показываем по 2 статьи на странице

    page_number = request.GET.get('page')  # Получаем номер страницы из параметра GET
    page_obj = paginator.get_page(page_number)  # Получаем объект страницы

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

def create_post(request):
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
    post = get_object_or_404(Post, id=post_id, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})