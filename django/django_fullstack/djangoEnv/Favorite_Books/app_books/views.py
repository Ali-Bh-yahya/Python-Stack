from django.shortcuts import *
from  .models import *
from . import models
from django.contrib import messages
# Create your views here.
def show_book(request):
  context = {
    'books':models.get_books()
  }
  
  return HttpResponse("home")
def add_book(request):
  if request.method == 'POST':
    errors = Book.objects.validation_book(request.POST)
    if len(errors) > 0:
      for key, value in errors.items():
          messages.error(request, value)
      return redirect('/')
    models.create_books(request.POST)
    return redirect('home')
  else:
    return HttpResponse("OPPS! Something went wrong")