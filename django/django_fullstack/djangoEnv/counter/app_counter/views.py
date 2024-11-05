from django.shortcuts import render,redirect

# Create your views here.
def root(request):
  return redirect('/')


def counter(request):
  if 'views' not in request.session:
    request.session['counter'] = 0
    request.session['views'] = 0
  request.session['views'] += 1
  return render(request,'index.html') 

def destroy_session(request):
  request.session.clear()
  return redirect('/')

def handle_action(request):
  if request.POST['btn'] == 'add2':
    request.session['counter'] += 2
  elif request.POST['btn'] == 'reset':
    request.session.clear()
  return redirect('/')