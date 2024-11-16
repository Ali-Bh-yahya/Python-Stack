from django.shortcuts import render , redirect
from django.contrib import messages
from . import models

# Create your views here.
def update_blog(request,id):
  if request.method == 'POST':
    errors = models.basic_validation(request.POST)
    if len(errors) > 0 :
     for key , value in errors.items():
       messages.error(request.value)
     return redirect(f'/blog/edit/{id}')
    else :
      