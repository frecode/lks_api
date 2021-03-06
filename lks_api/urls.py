"""lks_api URL Configuration

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
from django.urls import path, include, re_path
from app01.views import init_web, web_view
from django.views import static
from lks_api.settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app01.urls')),
    path('', web_view),
    path('web_view/', web_view),
    # path('init_web/', init_web),
    re_path('^static/(?P<path>.*)$', static.serve, {'document_root': STATIC_ROOT}, name='static'),
]
