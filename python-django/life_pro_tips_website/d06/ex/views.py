from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm, LoginForm
from .models import User
from django.conf import settings
import random

class Home(View):
    def get(self, request, *args, **kwargs):
        name: str
        if (request.session["is_active"]):
            name = request.session["name"]
        else:
            name = getattr(settings, 'DEFAULT_NAMES')[random.randint(0, 9)]
        return render(request, 'home.html', {"name": name, 'is_active': request.session["is_active"]})
    def post(self, request, *args, **kwargs):
        if 'action' in request.POST and request.POST['action'] == 'logout':
            request.session['is_active'] = False
            return redirect('login_view')
    
class DataApi(View):
    def get(self, request, *args, **kwargs):
        names = getattr(settings, 'DEFAULT_NAMES')
        rand_value = random.randint(0, 9)
        return JsonResponse({'name': names[rand_value]})
    
class Login(View):
    def get(self, request, *args, **kwargs):
        if (request.session["is_active"]):
            return redirect('home_view')
        login_form = LoginForm()
        return render(request, 'login.html', {"login_form": login_form})
    def post(self, request, *args, **kwargs):
        error = [False, '']
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data['user_name']
            password = login_form.cleaned_data['password']
            user_not_exit = False
            try:
                db_user_name = User.objects.get(name=name)
            except User.DoesNotExist :
                user_not_exit = True
            if user_not_exit:
                error = [True, 'User / Password Wrong']
            else:
                if db_user_name.password != password:
                    error = [True, 'User / Password Wrong']
                else:
                    request.session["is_active"] = True
                    request.session["name"] = name
                    return redirect('home_view')
        return render(request, 'login.html', {"login_form": login_form, "error": error[1]})

class Registration(View):
    def get(self, request, *args, **kwargs):
        if (request.session["is_active"]):
            return redirect('home_view')
        registration_form = RegistrationForm()
        return render(request, 'registration.html', {"registration_form": registration_form})
    def post(self, request, *args, **kwargs):
        error = [False, '']
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            name = registration_form.cleaned_data['user_name']
            password = registration_form.cleaned_data['password']
            password_confirmation = registration_form.cleaned_data['password_confirmation']
            db_is_empty = False
            try:
                db_user_name = User.objects.get(name=name)
            except User.DoesNotExist :
                db_is_empty = True
            if password != password_confirmation:
                error = [True, 'Password Not Identic.']
            elif not db_is_empty:
                error = [True, 'User Already Exist.']
            else:
                User.objects.create(name=name, password=password, is_logged=True)
                request.session["is_active"] = True
                request.session["name"] = name
                return redirect('home_view')
            return render(request, 'registration.html', {"registration_form": registration_form, "error": error[1]})
            




