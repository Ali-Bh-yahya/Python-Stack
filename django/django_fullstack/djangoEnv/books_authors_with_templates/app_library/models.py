from django.db import models

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length = 25)
  last_name = models.CharField(max_length = 25)
  note = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  #books = models.ManyToManyField(Author , related_name = "authors" )

class Book(models.Model):
  title =models.CharField(max_length=39)
  description = models.TextField()
  authors = models.ManyToManyField(Author , related_name = "books" )
  created_at  = models.DateTimeField(auto_now_add = True )
  updated_at = models.DateTimeField(auto_now  = True )

## this functin will get the book including by users
def get_books():
  books = Book.objects.all()
  return books

## this functin will create the book  getting from the get function
def add_books(data):
  Book.objects.create(title = data['title'], description = data['desc'])


def get_authors():
  authors = Author.objects.all()
  return authors

def add_authors(data):
  Author.objects.create(first_name = data['first_name'],last_name = data['last_name'], note = data['note'])

def view_fun_book(id):
   return Book.objects.get(id = id)

def view_fun_author(id):
  return Author.objects.get(id = id)

def add_author_to_book_confirm(data):
  this_book = Book.objects.get(id = data["book"])
  this_author = Author.objects.get(id = data["author"])
  this_book.authors.add(this_author)

def add_books_to_author(data):
  book = Book.objects.get(id = data['book'])
  author = Author.objects.get(id = data["author"])
  author.books.add(book)
