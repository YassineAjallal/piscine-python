from django.urls import path
from .views import Articles, Home, Login, Publications, Details
urlpatterns = [
    path('', Home.as_view(), name='home_view'),
    path('articles/', Articles.as_view(), name='articles_view'),
    path('publications/', Publications.as_view(), name='publications_view'),
    path('details/<int:pk>/', Details.as_view(), name='details_view'),
    path('login/', Login.as_view(), name='login_view')
]