from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from .models import Registration
from . import models
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def register_user(request):
    if request.method == 'POST':
        errors = Registration.objects.validate_registration(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        models.save_data_for_reg(request.POST)
        return redirect('/')
    return HttpResponseRedirect('Something went wrong. Please try again!')


def login_user(request):
    if request.method == 'POST':
        errors = Registration.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='login')
            return redirect('/')
        email = request.POST['email']
        user = Registration.objects.get(email=email)
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        return redirect('/success')
    return HttpResponse('Something went wrong. Please try again!')


def success_user(request):
    return render(request, 'success.html')


def logout_user(request):
    request.session.clear()
    return redirect('/')
