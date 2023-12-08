from django.urls import path
from ex09.views import Display

urlpatterns = [
    path('display/', Display.as_view())
]