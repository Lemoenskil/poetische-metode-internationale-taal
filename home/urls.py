from .views import index, about, contact, learning_methode
from django.urls import path, re_path
from django.shortcuts import redirect
from home import views

urlpatterns = [
    path('', lambda request: redirect('index.html', permanent=False)),
    path('index.html', views.index, name='index'),
    re_path(r'about/', about, name='about'),
    re_path(r'learning_methode/', learning_methode, name='learning_methode'),
    re_path(r'contact/', contact, name='contact'),
]