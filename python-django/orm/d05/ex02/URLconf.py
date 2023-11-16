from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.building_a_table),
    path('populate/', views.insert_in_tabel),
    path('display/', views.display)
]