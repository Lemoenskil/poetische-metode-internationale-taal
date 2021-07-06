"""poetische_metode_internationale_taal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls.conf import include, path, re_path
from django.conf import settings           
from home.urls import urlpatterns as index_paths
from poems.urls import urlpatterns as poems_paths
from blogs.urls import urlpatterns as blogs_paths
from search.urls import urlpatterns as search_paths
from django.conf.urls.static import static
from django.views.generic import RedirectView
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'',include(index_paths)),
    re_path(r'poems/',include(poems_paths)),
    re_path(r'blogs/', include(blogs_paths)),
    re_path(r'search/', include(search_paths)),
]

USE_S3 = os.getenv('USE_S3') == 'TRUE'
if not USE_S3:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

