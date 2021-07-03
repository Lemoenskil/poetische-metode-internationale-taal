from django.conf.urls import url
from .views import get_blogs
# blog_detail, create_or_edit_blog

urlpatterns = [
    url(r'^$', get_blogs, name='get_blogs'),
    # url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    # url(r'^new/$', create_or_edit_post, name='new_post'),
    # url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post')
]