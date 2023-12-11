from django.urls import path
from .views import Home, Login, Registration, DataApi
urlpatterns = [
    path('', Home.as_view(), name='home_view'),
    path('api/', DataApi.as_view()),
    path('login/', Login.as_view(), name="login_view"),
    path('registration/', Registration.as_view(), name="registration_view")
]