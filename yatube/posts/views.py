from multiprocessing import context
from re import template
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    context={
        'title': 'ЭТО тайтл из вьюхи',
        'text': 'Это главная страница'
    }
    return render(request, template, context=context)

def groups(request):
    template = 'posts/groups.html'
    return render(request, template_name=template)

def group_list(request):
    template = 'posts/group_list.html'
    context={
        'title': 'ЭТО тайтл из вьюхи',
        'text': 'Здесь будет информация о группа проекта Yatube'
    }
    return render(request, template, context=context)
