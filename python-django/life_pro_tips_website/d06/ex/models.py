from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=64, null=False)
    is_logged = models.BooleanField(default=False)

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)
    upvote = models.ManyToManyField(User, related_name='upvote')
    downvote = models.ManyToManyField(User, related_name='downvote')