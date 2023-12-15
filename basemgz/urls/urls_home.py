from django.urls import path 
from basemgz.views import views_home as views 

urlpatterns = [
    path('', views.home, name = 'home'),
]
