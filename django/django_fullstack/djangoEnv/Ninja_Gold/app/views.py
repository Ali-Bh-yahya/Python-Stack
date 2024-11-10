from django.shortcuts import *

from random import randint
# Create your views here.
def root(request):
  return redirect('/')
def index(request):
  if "Gold" not in request.session:
    request.session["Gold"] = 0
    request.session["massages"] = []
  return render(request,"index.html")

def prosses(request):
  # key = request.POST.get["key_of_place"]
  if request.method == 'POST':
    # print(key)

    if request.POST["key_of_place"] == "farm":
      gold_farm = randint(10,20)
      request.session['Gold'] += gold_farm
      message = f'Earned {request.session["Gold"]} from the farm!'
      request.session["massages"].append(message)
      print(request.session["massages"])

    elif request.POST['key_of_place'] == "cave":
      gold_cave = randint(5,10)
      request.session['Gold'] += gold_cave
      message = f'Earned {request.session["Gold"]} from the cave!'
      request.session["massages"].append(message)

    elif request.POST["key_of_place"] == "house":
      gold_house = randint(5,10)
      request.session['Gold'] += gold_house
      message = f'Earned {request.session["Gold"]} from the house!'
      request.session["massages"].append(message)

    elif request.POST["key_of_place"] == "casino":
      gold_casino = randint(-50,50)
      request.session["Gold"] += gold_casino
      if gold_casino > 0 :
        message = f'Earned {request.session["Gold"]} from the casino!'
        request.session["massages"].append(message)

      elif gold_casino < 0 :
        message = f'Lost {abs(request.session["Gold"])} from the casino!'
        request.session["massages"].append(message)
    return redirect('/')
  
  elif request.method == 'GET':
    context={
      "error": "Oppes somothing is wrong"
    }
    return render( request ,"error.html" , context)