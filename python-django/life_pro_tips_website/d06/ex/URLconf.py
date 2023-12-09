from django.urls import path
from .views import Display, DataApi
urlpatterns = [
    path('', Display.as_view()),
    path('api/', DataApi.as_view())
]