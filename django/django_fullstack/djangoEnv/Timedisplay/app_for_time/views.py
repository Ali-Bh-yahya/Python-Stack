from django.shortcuts import render,redirect
from datetime import datetime

# Create your views here.

def index(request):
  return redirect('/display_time')

def time_display(request):
  jenin = datetime.now ()
  context = {
    'time' : jenin.strftime("%Y-%m-%d %H:%M:%S")
  }
  
  return render(request,'index.html', context)