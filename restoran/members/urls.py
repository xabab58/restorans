from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings


app_name = 'members'

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user')

]
