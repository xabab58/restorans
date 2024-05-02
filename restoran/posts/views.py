from django.http import HttpResponse
from django.shortcuts import redirect, render


from .forms import *
from .models import restorans

from django.db import IntegrityError

def index(request):
    list = restorans.objects.all()
    context = {
        'restorans': list,
    }
    print(context)
    return render(request, 'posts/index.html', context)

def add_restoran(request):
    if request.method == "POST":
        form = AddRestoranForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('posts:index')
            except IntegrityError as e:
                form.add_error(None, f'Ошибка добавления: {e}')
    else:
        form = AddRestoranForm()
    return render(request, 'posts/add_restoran.html', {'form': form})


def help(request):
    return render(request, 'posts/help.html')

def id_restoran(request, slug):
    return HttpResponse('конкретный ресторан')
