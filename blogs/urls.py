from django.urls import path, re_path
from .views import get_blogs, blog_detail
#create_or_edit_blog

urlpatterns = [
    path('', get_blogs, name='get_blogs'),
    re_path(r'^(?P<pk>.+)$', blog_detail, name='blog_detail'),
    # path(r'^new/$', create_or_edit_post, name='new_post'),
    # re_path(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]