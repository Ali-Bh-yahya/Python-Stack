from django.shortcuts import render ,redirect

# Create your views here.
def index(request):
  return render(request,"index.html")

def prosses(request):
  if request.method == 'POST':
    return redirect()
  elif request.method == 'GET':
    context={
      "error": "Oppes somothing is wrong"
    }
    return render(request, context)