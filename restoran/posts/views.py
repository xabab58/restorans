from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Avg


from .forms import *
from .models import restorans

from django.db import IntegrityError

def index(request):
    restaurants_with_ratings = restorans.objects.annotate(avg_rating=Avg('score__rating'))
    reting=restorans.objects.annotate(avg_rating=Avg('score__rating')).order_by('-avg_rating').values('name')
    # top_one=reting[0]
    # top_two=reting[1]
    # top_three=reting[2]
    for restaurant in restaurants_with_ratings:
        print(f"Ресторан: {restaurant.name}, Средний рейтинг: {restaurant.avg_rating}, Картинка: {restaurant.image.url if restaurant.image else 'Нет изображения'}")

    rating_list = reting.values_list()
    
    names = [restaurant['name'] for restaurant in reting]
    print('rating1111111111111111111111',names)
    context = {
        'restaurants_with_ratings':restaurants_with_ratings,
        # 'top_one':top_one,
        # 'top_two':top_two,
        # 'top_three':top_three,
        'reting':reting,
        'names':names,
    }

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

def add_score(request):
    if request.method == "POST":
        form = AddScoreForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('posts:index')
            except IntegrityError as e:
                form.add_error(None, f'Ошибка добавления: {e}')
    else:
        form = AddScoreForm()
    return render(request, 'posts/add_score.html', {'form': form})


def help(request):
    return render(request, 'posts/help.html')

def id_restoran(request, slug):
    return HttpResponse('конкретный ресторан')


