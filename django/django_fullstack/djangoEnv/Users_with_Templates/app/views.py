from django.shortcuts import render,redirect,HttpResponse

from . import models

# Create your views here.
def index(request):
  context = {
    'users': models.add_data()
  }
  return render(request,'index.html',context)

def user_create(request):
  if request.method == 'POST':
   models.user_create(request.POST)   
   return redirect('/')
  elif request.method == 'GET':
    return HttpResponse('somthing wrong')
  
def user_delete(request, id):
  models.remove_user(id)
  return redirect('/')