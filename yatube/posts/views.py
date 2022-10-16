from getpass import getuser
from operator import ge
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Group, Post

from django.contrib.auth import get_user_model

from .forms import CreationForm

from django.contrib.auth.models import User

from django.core.mail import send_mail

AMOUNT_POSTS: int = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, AMOUNT_POSTS) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    paginator = Paginator(group.posts.all(),AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context=context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    paginator = Paginator(Post.objects.filter(author=author).all(), AMOUNT_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    post = get_object_or_404(Post, id=post_id)
    post_count = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'post_count': post_count,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data, author_id=request.user.id)
            return redirect('/profile/' + request.user.username)
    else:
        form = CreationForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)

def post_edit(request, post_id):
    if (request.user.is_authenticated) and (Post.objects.get(id=post_id).author_id == request.user.id):
        if request.method == 'POST':
            
        #вернуть апдейт поста
        return HttpResponse('Проверка условия на юзера работает')
    return redirect('/posts/' + str(post_id))