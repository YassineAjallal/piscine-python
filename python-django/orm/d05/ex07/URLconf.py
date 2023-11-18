from django.urls import path
from ex07 import views

urlpatterns = [
    path('populate/', views.insert_in_table),
    path('display/', views.display),
    path('update/', views.update)
]