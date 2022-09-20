from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_without_params(request):
    return HttpResponse(f'Группировка без параметров')

def group_posts_with_params(request, params):
    return HttpResponse(f'Группировка с параметрами: {params}')