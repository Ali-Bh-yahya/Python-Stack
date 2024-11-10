from django.shortcuts import render , HttpResponse
from . import models
# Create your views here.
def index(request):
  context = {
    'authors': models.Author.objects.all(),
  }
  return render(request,"index.html",context)