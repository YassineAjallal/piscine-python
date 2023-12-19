from django.urls import path
from .views import Articles, Home
urlpatterns = [
    path('', Home.as_view(), name='home_view'),
    path('articles/', Articles.as_view(), name='articles_view')
]