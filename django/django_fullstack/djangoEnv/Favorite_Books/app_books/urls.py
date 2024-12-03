from django.urls import path

from . import views 

urlpatterns = [
   path('', views.add_book),
   path('books/<int:id>',views.show_book)

]