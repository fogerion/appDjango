from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    #return HttpResponse('Home page')
    context: dict = {
        'title': 'Home-Главная',
        'content': 'Магазин мебели FOGER',
        
    }
    return render(request, 'main/index.html', context)

def about(request):
    context: dict = {
        'title': 'Home-О нас',
        'content': 'Обо нас',
        'text_on_page': "Хороший магазин товаров"
    }
    return render(request, 'main/about.html', context)