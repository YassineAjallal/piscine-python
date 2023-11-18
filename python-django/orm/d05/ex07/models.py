from django.db import models

from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=64, null=False)
    episode_nb = models.PositiveIntegerField(primary_key=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return (self.title)
