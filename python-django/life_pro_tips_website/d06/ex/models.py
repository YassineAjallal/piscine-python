from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
# Create your models here.
class CustomUser(AbstractUser):
    nb_points = models.IntegerField(null=False, default=0)
    def can_downvote_tip(self):
        if self.nb_points >= 15 and (not self.has_perm('ex.downvote_tip')):
            permission = Permission.objects.get(codename='downvote_tip')
            self.user_permissions.add(permission)
        elif (self.nb_points < 15 and self.has_perm('ex.downvote_tip')):
            permission = Permission.objects.get(codename='downvote_tip')
            self.user_permissions.remove(permission)
        return self.has_perm('ex.downvote_tip')
    def can_delete_tip(self):
        if (self.nb_points >= 30 and not self.has_perm('ex.delete_tip')):
            permission = Permission.objects.get(codename='delete_tip')
            self.user_permissions.add(permission)
        elif (self.nb_points < 30 and self.has_perm('ex.delete_tip')):
            permission = Permission.objects.get(codename='delete_tip')
            self.user_permissions.remove(permission)
        return self.has_perm('ex.delete_tip')
    

class Tip(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=64)
    date = models.DateField(auto_now=True)
    upvote = models.ManyToManyField(CustomUser, related_name='upvote')
    downvote = models.ManyToManyField(CustomUser, related_name='downvote')
    class Meta:
        permissions = (("downvote_tip", "can downvote a tip"),)