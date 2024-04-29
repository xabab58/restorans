from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    title = 'Главная страница'
    context = {

        'title': title,

        'text': 'Главная страница',
    }
    return render(request, 'posts/index.html', context)

def list_restorans(request):
    return HttpResponse('список ресторанов')

def id_restoran(request, slug):
    return HttpResponse('конкретный ресторан')
