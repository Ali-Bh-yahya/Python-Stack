from django.urls import path

from . import views

urlpatterns = [
  path('', views.index),
  path('register', views.register_user),
  path('login', views.login_user),
  path('dashboard', views.dashboard_user),
  path('dashboard_view',views.dashboard_view),
  path('pies/edit/<int:id>', views.dashboard_edit),
  path('pies/<int:id>/destroy',views.destroy),
  path('pies/update', views.dashboard_update),
  path('pies', views.dashboard_Baker),
  path('logout' , views.logout_user),
]