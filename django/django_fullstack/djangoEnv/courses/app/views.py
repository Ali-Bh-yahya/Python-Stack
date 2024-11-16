from django.shortcuts import *

from . import models
# Create your views here.
def courses(request):
  return HttpResponse("fuck you !!!")

def add_the_courses(request):
  return HttpResponse("I am here to add a course.")
