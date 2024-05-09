from django.shortcuts import redirect, render
from django.db.models import Avg, Count, Max, Min
from .forms import *
from .models import restorans
from django.contrib.auth.decorators import login_required
import random

from django.db import IntegrityError

def index(request):
    # restaurants_with_ratings = restorans.objects.annotate(avg_rating=Avg('score__rating'))
    # top_three = Score.objects.values('name_restoran__name').annotate(avg_rating=Avg('rating'), total_ratings=Count('rating')).order_by('-avg_rating', '-total_ratings')[:3]
    # random_restaurants = random.sample(restaurants_with_ratings, min(len(restaurants_with_ratings), 3))

    restaurants_with_ratings = list(restorans.objects.annotate(avg_rating=Avg('score__rating')))
    top_three = Score.objects.values('name_restoran__name').annotate(avg_rating=Avg('rating'), total_ratings=Count('rating')).order_by('-avg_rating', '-total_ratings')[:3]
    # random_restaurants = random.sample(restaurants_with_ratings, min(len(restaurants_with_ratings), 3))
    random.shuffle(restaurants_with_ratings)
    
    context = {
        'restaurants_with_ratings':restaurants_with_ratings,
        'top_three':top_three,

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
                score = form.save(commit=False)
                if request.user.is_authenticated:
                    score.name = request.user.username
                score.save()
                return redirect('posts:index')
            except IntegrityError as e:
                form.add_error(None, f'Ошибка добавления: {e}')
    else:
        if request.user.is_authenticated:
            initial_data = {'name': request.user.username}
            form = AddScoreForm(initial=initial_data)
        else:
            form = AddScoreForm()
    return render(request, 'posts/add_score.html', {'form': form})


# def add_score(request):
#     if request.method == "POST":
#         form = AddScoreForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('posts:index')
#             except IntegrityError as e:
#                 form.add_error(None, f'Ошибка добавления: {e}')
#     else:
#         form = AddScoreForm()
#     return render(request, 'posts/add_score.html', {'form': form})


def help(request):
    return render(request, 'posts/help.html')

def id_restoran(request, id):
    
    zakazi = Score.objects.filter(name_restoran_id=id)
    all_score = zakazi.count()

    get_restoran = restorans.objects.get(id=id)
    restoran_name = get_restoran.name
    latest_score = Score.objects.latest('data')
    last_date = latest_score.data
    formatted_last_date = last_date.strftime("%d.%m.%Y")
    all_table = Score.objects.all()
    all_table = Score.objects.filter(name_restoran=id).order_by('-data')
    max_rating = Score.objects.aggregate(max_rating=Max('rating'))['max_rating']
    min_rating = Score.objects.aggregate(min_rating=Min('rating'))['min_rating']
    avg_rating = Score.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
    






    context={
        'zakazi': zakazi,
        'all_score': all_score,
        'restoran_name': restoran_name,
        'formatted_last_date': formatted_last_date,
        'get_restoran': get_restoran,
        'all_table': all_table,
        'max_rating': max_rating,
        'min_rating': min_rating,
        'avg_rating': avg_rating,
    }
    return render(request, 'posts/id_restoran.html', context )


