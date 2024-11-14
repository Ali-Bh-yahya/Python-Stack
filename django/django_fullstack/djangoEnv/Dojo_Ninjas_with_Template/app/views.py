from django.shortcuts import *

from . import models
# Create your views here.

def index(request):
    context ={
      'dojos':models.get_dojos(),
    }
    return render(request,'index.html',context)

def add_dojo(request):
    if request.method == "POST":
      models.create_dojo(request.POST)
      return redirect('/')
    elif request.method == "Get":
       return HttpResponse("something wrong")
    
def add_ninja(request):
    if request.method == "POST":
      models.create_ninja(request.POST)
      return redirect('/')
    elif request.method == "Get":
       return HttpResponse("something wrong")
