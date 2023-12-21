from typing import Any
from django.urls import reverse_lazy
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
        context['publications'] = Article.objects.filter(author__username=str(self.request.user))
        return context


    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)

class Favourites(TemplateView):
    template_name = 'favourites.html'
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('login_view')
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        favourites = UserFavouriteArticle.objects.filter(user__username=str(self.request.user))
        context['favourites'] = [favourite.article for favourite in favourites]
        return context


    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)

class Details(DetailView, CreateView):
    
    model = Article
    template_name='details.html'
    context_object_name = 'article'
    form_class = AddToFavouriteForm
    article_object: Article
    pk: int

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            try:
                user = UserFavouriteArticle.objects.get(user=self.request.user, article=self.get_object())
                context['already_liked'] = True
            except UserFavouriteArticle.DoesNotExist:
                context['already_liked'] = False
        return context
    def get_success_url(self):
        return reverse_lazy('details_view', kwargs={'pk': self.pk})

    def post(self, request, *args, **kwargs):
        if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
            logout(request)
            return redirect('login_view')
        self.article_object = self.get_object()
        self.pk = self.get_object().pk
        self.model = UserFavouriteArticle
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            user = UserFavouriteArticle.objects.get(user=self.request.user, article=self.article_object)
            user.delete()
            return redirect(self.get_success_url())
        except UserFavouriteArticle.DoesNotExist:
            form.instance.user = self.request.user
            form.instance.article = self.article_object
        response = super(CreateView, self).form_valid(form)
        return response

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


