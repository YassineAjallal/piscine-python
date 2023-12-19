from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Article
from django.contrib.auth.models import User

class Articles(TemplateView):
    template_name = 'articles.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context
    

class Home(RedirectView):
    pattern_name = 'articles_view'
    permanent = False
    query_string = False
    def get_redirect_url(self, *args: Any, **kwargs: Any):
        return super().get_redirect_url(*args, **kwargs)
    
class Login():