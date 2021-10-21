from django.urls import path, re_path
from .views import get_audio
#create_or_edit_

urlpatterns = [
    path('', get_audio, name='audio'),
]