from django.urls import path
from . import views

urlpatterns = [
  path('',views.index),
  path('display_time', views.time_display),

]