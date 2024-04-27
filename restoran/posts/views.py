from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('главная страница')

def list_restorans(request):
    return HttpResponse('список ресторанов')

def id_restoran(request):
    return HttpResponse('конкретный ресторан')
