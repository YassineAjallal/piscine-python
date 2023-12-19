from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=64, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=False)
    synopsis = models.CharField(max_length=312, null=False)
    content = models.TextField(null=False)
    def __str__(self) -> str:
        return self.title
    
class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.article.title