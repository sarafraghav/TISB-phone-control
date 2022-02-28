

from django.urls import path
from django.views.generic.base import TemplateView
from . import views

#Defines all models 
urlpatterns = [
    path('home/', views.home, name="home"),  


 ]


