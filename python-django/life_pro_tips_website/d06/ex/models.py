from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)
    upvote = models.ManyToManyField(CustomUser, related_name='upvote')
    downvote = models.ManyToManyField(CustomUser, related_name='downvote')