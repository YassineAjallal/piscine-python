from django.urls import path

from . import views

urlpatterns = [
    path("", views.helloworld, name="helloworld"),
]