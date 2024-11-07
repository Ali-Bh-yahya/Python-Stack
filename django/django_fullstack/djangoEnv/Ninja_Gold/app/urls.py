from django.urls import path

from . import views

urlpatterns = [
  path('',views.index),
  path('prosses_money', views.prosses)
]