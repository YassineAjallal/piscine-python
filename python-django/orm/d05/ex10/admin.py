from django.contrib import admin
from .models import Planets, People, Movies

# Register your models here.
admin.site.register(Planets)
admin.site.register(People)
admin.site.register(Movies)
