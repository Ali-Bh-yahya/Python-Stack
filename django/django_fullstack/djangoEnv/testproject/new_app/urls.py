from django.urls import path 
from . import views

# urlpatterns = [
#   path('', views.show_template),
#   path('request',views.some_fun)

# ]

urlpatterns = [
  path('', views.index),
  path('users', views.user)
]