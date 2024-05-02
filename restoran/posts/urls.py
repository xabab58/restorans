from django.urls import path
from . import views


from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_restoran', views.add_restoran, name='add_restoran'),
    path('help', views.help, name='help'),
    path('id/<slug:slug>/', views.id_restoran),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)