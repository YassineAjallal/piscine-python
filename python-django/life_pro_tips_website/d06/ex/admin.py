from django.contrib import admin
from .models import CustomUser, Tip
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    pass
admin.site.register(CustomUser)
admin.site.register(Tip)
