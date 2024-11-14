from django.urls import path

from . import views

urlpatterns = [
  path('', views.get_fun_book),
  path('authors', views.get_fun_author),
  path('add_book', views.add_fun_book),
  path('add_author', views.add_fun_author),
  path('show_book/<int:id>', views.fun_book),
  path('show_author/<int:id>', views.fun_author),
  path('join', views.add_authors_to_book),
  path('join_author', views.add_books_to_author)
]