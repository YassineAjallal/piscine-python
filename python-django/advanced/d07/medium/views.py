from typing import Any
from django.http import HttpRequest, HttpResponse, HttpResponse as HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import Article

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
    
class Details(DetailView):
    model = Article
    template_name='details.html'
    context_object_name = 'article'
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if self.request.method == 'POST':
            if 'action' in self.request.POST and self.request.POST['action'] == 'logout':
                logout(request)
                return redirect('login_view')
        return super().dispatch(request, *args, **kwargs)
    