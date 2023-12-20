from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, AddToFavouriteForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Article, UserFavouriteArticle


class Articles(TemplateView):
    template_name = 'articles.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)

class Home(RedirectView):
    pattern_name = 'articles_view'
    permanent = False
    query_string = False

    def get_redirect_url(self, *args: Any, **kwargs: Any):
        return super().get_redirect_url(*args, **kwargs)
    
class Login(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('home_view')
        return super().get(request, *args, **kwargs)


    def form_valid(self, form: Any) -> HttpResponse:
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
class Publications(TemplateView):
    template_name = 'publications.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('login_view')
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        print(self.request.user)
        context['publications'] = Article.objects.filter(author__username=str(self.request.user))
        return context


    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)

class AddToFavourite(CreateView):
    model = UserFavouriteArticle
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return Details.as_view()
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        print('here')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)

class Details(DetailView, CreateView):
    model = Article
    template_name='details.html'
    context_object_name = 'article'
    form_class = AddToFavouriteForm
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super(CreateView, self).dispatch(request, *args, **kwargs)

class Register(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    model = User
    success_url ='/'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('home_view')
        return super().get(request, *args, **kwargs)


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        valid = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


class Publish(CreateView):
    template_name = 'publish.html'
    model = Article
    success_url = '/'
    fields = ['title', 'synopsis', 'content']

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('home_view')
        return super().get(request, *args, **kwargs)
    

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)


