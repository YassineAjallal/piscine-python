from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.http import  JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Permission
from .forms import TipsForm, CustomAuthenticationForm, CustomUserCreationForm
from .models import CustomUser, Tip
import random

# class that hold tip information to easly read it from template
class TipInfo:
    def __init__(self, id, content, author, date, upvotes, downvotes) -> None:
        self.id = id
        self.content = content
        self.author = author
        self.date = date
        self.upvotes = upvotes
        self.downvotes = downvotes

class Home(View):
    def get(self, request, *args, **kwargs):
        name = getattr(settings, 'DEFAULT_NAMES')[random.randint(0, 9)]
        nb_points = 0
        tips_form = TipsForm()
        all_tips = [TipInfo(tip.id, tip.content, tip.author, tip.date, tip.upvote.all().count(), tip.downvote.all().count()) 
                    for tip in Tip.objects.all()]
        if (request.session.get("_auth_user_id")):
            name = request.user
            try:
                nb_points = CustomUser.objects.get(username=name).nb_points
            except CustomUser.DoesNotExist:
                nb_points = 0
        # else:
        #     name = getattr(settings, 'DEFAULT_NAMES')[random.randint(0, 9)]
        return render(request, 'home.html', {"tips_form": tips_form,
                                                "name": name,
                                                'nb_points': nb_points,
                                                'is_active': request.session.get("_auth_user_id"),
                                                'all_tips' : all_tips})
    def post(self, request, *args, **kwargs):
        if 'action' in request.POST and request.POST['action'] == 'logout':
            logout(request)
            return redirect('login_view')
        elif 'tip_id' in request.POST:
            tip_id = int(request.POST.get('tip_id'))
            if request.POST['action'] == 'upvote' or request.POST['action'] == 'downvote':
                return self.vote(request, request.POST['action'], tip_id)
            elif request.POST['action'] == 'delete':
                return self.delete_tip(request, tip_id)
        else:
            return self.add_tip(request)
    # add new tip
    def add_tip(self, request):
        tips_form = TipsForm(request.POST)
        if tips_form.is_valid() and request.session.get('_auth_user_id'):
            user = CustomUser.objects.get(username=request.user)
            content = tips_form.cleaned_data['content']
            tip = Tip(content=content, author=request.user)
            tip.save()
            user.tips.add(tip)

        return redirect('home_view')

    # affect upvote or downvote in a selected tip
    def vote(self, request, action, tip_id):
        selected_tip = Tip.objects.get(id=tip_id)
        tip_owner = CustomUser.objects.get(username=selected_tip.author)
        already_upvote = True
        already_downvote = True
        user = CustomUser.objects.get(username=request.user)
        try:
            selected_tip.upvote.get(username=user.username)
        except:
            already_upvote = False
        try:
            selected_tip.downvote.get(username=user.username)
        except:
            already_downvote = False
        if action == 'upvote':
            if (not already_upvote):
                if (str(request.user) != str(tip_owner.username)):
                    tip_owner.nb_points += 5
                    tip_owner.save()
                selected_tip.upvote.add(user)
                if already_downvote:
                    selected_tip.downvote.remove(user)
            else:
                selected_tip.upvote.remove(user)
        else:
            if user.username == selected_tip.author or user.has_perm('ex.downvote_tip'):
                if (not already_downvote):
                    if (request.user != tip_owner.username):
                        if (tip_owner.nb_points < 2):
                            tip_owner.nb_points = 0
                        else:
                            tip_owner.nb_points -= 2
                    tip_owner.save()
                    selected_tip.downvote.add(user)
                    if already_upvote:
                        selected_tip.upvote.remove(user)
                else:
                    selected_tip.downvote.remove(user) 
        
        if tip_owner.nb_points >= 15 and (not tip_owner.has_perm('ex.downvote_tip')):
            permission = Permission.objects.get(codename='downvote')
            tip_owner.user_permissions.add(permission)
            tip_owner.save()
        print(tip_owner.has_perm('ex.downvote_tip'))
        # elif (tip_owner.nb_points < 15 and tip_owner.has_perm('ex.downvote_tip')):
        #     permission = Permission.objects.get(codename='downvote')
        #     tip_owner.user_permissions.remove(permission)
        # if (tip_owner.nb_points >= 30 and not tip_owner.has_perm('ex.delete_tip')):
        #     permission = Permission.objects.get(codename='delete')
        #     tip_owner.user_permissions.add(permission)
        # elif (tip_owner.nb_points < 30 and tip_owner.has_perm('ex.delete_tip')):
        #     permission = Permission.objects.get(codename='delete')
        #     tip_owner.user_permissions.remove(permission)
        return redirect('home_view')

    def delete_tip(self, request, tip_id):
        selected_tip = Tip.objects.get(id=tip_id)
        user = CustomUser.objects.get(username=request.user)
        if user.username == selected_tip.author or user.has_perm('ex.delete_tip'):
            selected_tip.delete()
        return redirect('home_view')

class DataApi(View):
    def get(self, request, *args, **kwargs):
        names = getattr(settings, 'DEFAULT_NAMES')
        rand_value = random.randint(0, 9)
        return JsonResponse({'name': names[rand_value]})
    
class Login(View):
    def get(self, request, *args, **kwargs):
        if request.session.get('_auth_user_id'):
            return redirect('home_view')
        login_form = CustomAuthenticationForm()
        return render(request, 'login.html', {"login_form": login_form})
    def post(self, request, *args, **kwargs):
        error = [False, '']
        login_form = CustomAuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_view')
        return render(request, 'login.html', {"login_form": login_form})


class Registration(View):
    def get(self, request, *args, **kwargs):
        if request.session.get('_auth_user_id'):
            return redirect('home_view')
        registration_form = CustomUserCreationForm()
        return render(request, 'registration.html', {"registration_form": registration_form})
    def post(self, request, *args, **kwargs):
        registration_form = CustomUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save()
            login(request, user)
            return redirect('home_view')
        return render(request, 'registration.html', {"registration_form": registration_form})
            




