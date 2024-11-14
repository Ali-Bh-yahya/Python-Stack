from django.shortcuts import render , redirect, HttpResponse

from . import models
# Create your views here.


def get_fun_book(request):
  context = {
    'books' : models.get_books(),
  }
  return render(request, 'add_book.html', context)
def get_fun_author(request):
  context = {
    'authors' : models.get_authors(),
  }
  return render(request, 'add_author.html' , context)

def add_fun_book(request):
  if request.method == 'POST':
    models.add_books(request.POST)
    return redirect('/')
  else :
    return HttpResponse("Something wrong")
  
def add_fun_author(request):
  if request.method == 'POST':
    models.add_authors(request.POST)
    return redirect('/authors')
  else :
    return HttpResponse("Something wrong")
  

def fun_book(request,id):
  context = {
    'book' : models.view_fun_book(id),
    'authors' : models.get_authors(),

  }
  return render(request,'views_book.html', context)
 

def fun_author(request,id):
  context = {
    'author':models.view_fun_author(id),
    'books' : models.get_books()
  }
  return render(request,'views_author.html', context)

def add_authors_to_book(request):
  book_id = request.POST['book']
  models.add_author_to_book_confirm(request.POST)
  return redirect('/show_book/' + str(book_id))

def add_books_to_author(request):
  id = request.POST.get('author')
  models.add_books_to_author(request.POST)
  return redirect(f'show_author/{id}')  
