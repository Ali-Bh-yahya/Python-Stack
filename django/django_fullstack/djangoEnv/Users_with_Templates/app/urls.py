from django.urls import path
from . import views

urlpatterns= [
  path('',views.index),
  path('proces', views.user_create),
  path('delete/<int:id>', views.user_delete, name='delete'),
]