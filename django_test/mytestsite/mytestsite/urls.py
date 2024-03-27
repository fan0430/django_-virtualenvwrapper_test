"""
URL configuration for mytestsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from catalog import views, urls

from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 引入到app urls
    # path('catalog/', include('catalog.urls')),
    # path('', include('catalog.urls')),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
    

    # 导向未定义的 URL 到 views.page_not_found
    re_path(r'^.*', views.other),
    # re_path(r'^(?!admin/|catalog/).*', views.menu), # 用正則過濾已知

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

