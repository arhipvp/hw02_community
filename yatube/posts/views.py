from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')

def group_without_params(request):
    return HttpResponse(f'Группировка без параметров')

def group_posts_with_params(request, params):
    return HttpResponse(f'Группировка с параметрами: {params}')