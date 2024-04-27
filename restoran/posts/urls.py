from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list_restorans/', views.list_restorans),
    path('id/<slug:slug>/', views.id_restoran),

]
