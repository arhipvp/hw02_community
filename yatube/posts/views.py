from django.shortcuts import get_object_or_404, render
from .models import Group, Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, template, context=context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    template = 'posts/group_list.html'
    title = f'Записи сообщества {group.__str__()}'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context=context)
    
