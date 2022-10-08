from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    context = {
        'posts': Post.objects.order_by('-pub_date')[:10],
    }
    return render(request, template, context=context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': group.posts.order_by('-pub_date')[:10],
    }
    return render(request, template, context=context)
