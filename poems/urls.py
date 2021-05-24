from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.poems, name='poems'),
    re_path(r'^(?P<id>.+)$', views.single_poem, name='single_poem'),
]