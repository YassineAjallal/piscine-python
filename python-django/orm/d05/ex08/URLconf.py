from django.urls import path
from ex08 import views
urlpatterns = [
    path('init/', views.init),
    path('populate/', views.populate),
    path('display/', views.display)
]