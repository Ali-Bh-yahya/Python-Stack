from django.urls import path

from . import views

urlpatterns = [
  path('blogs/edite/<int:id>',views.update_blog,name= "update_blog"),
  path('blogs/',views.list_blogs , name = "list_blogs")
]