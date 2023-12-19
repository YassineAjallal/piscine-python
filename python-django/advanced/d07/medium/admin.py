from django.contrib import admin
from .models import Article, UserFavouriteArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(UserFavouriteArticle)
