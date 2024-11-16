from django.urls import path

from . import views

urlpatterns = [
  path('', views.courses),
  path('/add', views.add_the_courses)
]