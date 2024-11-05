from django.shortcuts import render , redirect

# Create your views here.

def root(request):
    return redirect('/')

def add_your_info(request):
    return render(request,'index.html')
def print_result(request):
  if request.method == 'POST':
    context = {
       'name': request.POST['name'],
      'location': request.POST['location'],
      'language' :request.POST['language'],
      'comment':  request.POST['comment']
      }
    return render(request, 'result.html',context)
  elif request.method == 'GET':
    return redirect('/')

