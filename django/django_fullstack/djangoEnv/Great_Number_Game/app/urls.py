from django.urls import *     
from . import views

urlpatterns = [
    path('', views.index),
    path('guess', views.compare_function),
    path('reset', views.reset)
    ]