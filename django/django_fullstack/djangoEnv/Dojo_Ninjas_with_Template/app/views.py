from django.shortcuts import render

from . import models
# Create your views here.

def index(request):
    context ={
      'dojos':models.add_dojo(),
      'ninjas': models.add_ninja() 
    }
    return render(request,'index.html',context)