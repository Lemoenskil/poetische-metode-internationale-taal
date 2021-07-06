from django.conf.urls import url
from django.contrib import admin
from . import views
from django.urls import include, path, re_path

urlpatterns = [
     path('', views.search, name='search'),
]