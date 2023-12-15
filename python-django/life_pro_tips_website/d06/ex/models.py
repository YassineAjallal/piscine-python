from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    tips = models.ManyToManyField('Tip')
    nb_points = models.IntegerField(null=False, default=0)

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)
    upvote = models.ManyToManyField(CustomUser, related_name='upvote')
    downvote = models.ManyToManyField(CustomUser, related_name='downvote')
    class Meta:
        permissions = (("downvote", "can downvote a tip"),)