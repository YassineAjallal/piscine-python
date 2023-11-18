"""
URL configuration for d05 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ex00/', include('ex00.URLconf')),
    path('ex02/', include('ex02.URLconf')),
    path('ex03/', include('ex03.URLconf')),
    path('ex04/', include('ex04.URLconf')),
    path('ex05/', include('ex05.URLconf')),
    path('ex06/', include('ex06.URLconf')),
    path('ex07/', include('ex07.URLconf')),
    path('ex08/', include('ex08.URLconf')),
]
