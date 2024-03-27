from django.urls import path, re_path
from . import views

# urlpatterns = [

# ]

urlpatterns = [
    path('', views.home, name='home'), 
    re_path(r'^home/$', views.home),
    path('menu/', views.menu),
    # path('home/', views.home, name='home'),
]