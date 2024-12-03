from django.shortcuts import *
from .models import *
from . import models
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        errors = User.objects.validate_registration(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        models.save_data_for_reg(request.POST)
        return redirect('/')
    return HttpResponse('Something went wrong. Please try again!')


def login_user(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='login')
            return redirect('/')
        email = request.POST['email']
        user = User.objects.get(email=email)
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        return redirect('/dashboard')
    return HttpResponse('Something went wrong. Please try again!')

def dashboard_user(request):
    if 'first_name' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    pies = models.get_pies_by_baker(request.session['user_id'])
    context = {
        'user' : user,
        'pies' : pies
    }
    return render(request, 'dashboard.html', context)
def dashboard_view(request):
    if request.method == 'POST':
        errors = Pies.objects.pies_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/dashboard')
        models.save_data_for_pies(request.POST,request.session)
        return redirect('/dashboard')
    return HttpResponse('Something went wrong. Please try again!')
def dashboard_edit(request ,id):
  

  context = {
  'pies': models.get_pie_by_id(id)
}
        
  return render(request,'edit.html',context)

def dashboard_update(request):
    if request.method == 'POST':
        errors = Pies.objects.pies_validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            pie_id = request.POST.get('id')
            # print(request.POST)
            return redirect(f'/pies/edit/{pie_id}')
        models.update_pies(request.POST)
        return redirect('/dashboard')
    return HttpResponse('Something went wrong. Please try again!')

def dashboard_Baker(request):
    context = {
        'pies': models.get_pies()
    }
    return render(request, 'baker.html', context)

def destroy(request, id):
    models.delete_pie(id)
    return redirect('/dashboard')
                

def logout_user(request):
    request.session.clear()
    return redirect('/')
