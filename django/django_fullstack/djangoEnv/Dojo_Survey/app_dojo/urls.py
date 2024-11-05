from django.urls import path
from . import views

urlpatterns = [
  path('',views.add_your_info),
  path('result/',views.print_result)
]