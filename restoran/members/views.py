from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import  UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:index')
        else:
            messages.success(request, ("Не верный логин или пароль, попробуйте еще раз.."))
            return redirect('members:login')
    else:
        return render(request, 'members/login.html', )

def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из системы!"))
    return redirect('posts:index')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            passworld = form.cleaned_data['password1']
            user = authenticate(username=username, password=passworld)
            login(request, user)
            messages.success(request, ("Успешно"))
            return redirect('posts:index')
    else:
        form = RegisterUserForm()

    return render(request, 'members/register_user.html' , {'form':form})