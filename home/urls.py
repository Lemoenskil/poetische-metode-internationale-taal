from .views import index, about, contact
from django.urls import path, re_path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'about/', about, name='about'),
    re_path(r'contact/', contact, name='contact'),
]