from django.shortcuts import get_object_or_404, render

from .models import Group, Post

AMOUNT_POSTS: int = 10


def index(request):
    context = {
        'posts': Post.objects.all()[:AMOUNT_POSTS],
    }
    return render(request, 'posts/index.html', context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    context = {
        'group': group,
        'posts': group.posts.all()[:AMOUNT_POSTS],
    }
    return render(request, 'posts/group_list.html', context=context)
