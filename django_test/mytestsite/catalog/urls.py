from django.urls import path, re_path
from . import views

# urlpatterns = [

# ]

urlpatterns = [
    path('', views.home, name='home'), 
    re_path(r'^home/$', views.home),
    path('menu/', views.menu, name ='test_menu'),
    # path('home/', views.home, name='home'),
    path('menu/<int:pk>', views.menu, name ='test_menu2'),
    path('add/', views.add, name ='add'),
    path('update/', views.update, name ='update'),
]