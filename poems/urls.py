from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.poems, name='poems'),
    path('poem', views.poems_detail, name='poems_detail'),
]