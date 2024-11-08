

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def article_list(request):
    articles = Post.objects.all()
    return render(request, 'blog/article_list.html', {'articlesscilk': articles})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

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