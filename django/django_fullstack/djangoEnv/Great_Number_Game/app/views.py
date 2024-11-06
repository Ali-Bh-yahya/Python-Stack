from django.shortcuts import render, HttpResponse , redirect
from random import randint
# Create your views here.
def index(request):
  if "num_rand" not in request.session:
    request.session["num_rand"] = randint(1,100)
  print(request.session["num_rand"])
  return render(request,'index.html')

def compare_function (request):
  gusses_num = int(request.POST['guess'])
  num_rand = request.session['num_rand']
  if gusses_num ==  num_rand:
    request.session['massage'] = f'{gusses_num} was the number'
    request.session["won"] = True
  if gusses_num > num_rand:
    request.session['massage'] = "is too high !"
  if gusses_num < num_rand:
     request.session['massage'] = "is too low !"
  return redirect('/')
    
def reset(request):
  request.session.clear()
  return redirect('/')