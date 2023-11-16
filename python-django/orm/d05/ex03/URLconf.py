from django.urls import path
from . import views
urlpatterns = [
    path('populate/', views.insert_in_table),
    path('display/', views.display)
]